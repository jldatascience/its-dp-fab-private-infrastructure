#!/usr/bin/env python3
"""validate-manifests.py — contrôle des manifestes proposés (aucune action sur Azure ou Fabric).

Contrôles :
  1. syntaxe YAML et champs obligatoires du schéma PROPOSÉ ;
  2. marqueurs ([A_RENSEIGNER], [A_VERIFIER], [A_CONFIRMER_MICK], [A_CONFIRMER_GLOBAL],
     [HORS_PERIMETRE_PRODUIT]) et leur caractère bloquant ;
  3. références : cibles de flux, identityRef, keyVaultRefs, patterns autorisés ;
  4. absence de valeur secrète ou d’adresse IP dans les manifestes ;
  5. calcul des approbations entrantes (flux déclarés par les autres manifestes) ;
  6. statut deployable recalculé (jamais vrai tant qu’un marqueur bloquant subsiste).

Sorties : documentation/manifest-validation-report.md et .html (manques en rouge),
          tracking/missing-parameters.csv.
Code retour : 0 si tous les manifestes sont syntaxiquement valides (même non déployables),
              1 en cas d’erreur structurelle.

Usage : python3 scripts/validate-manifests.py [--root .] [--strict]
        --strict : code retour 3 si au moins un manifeste n’est pas déployable.
"""
import argparse, csv, html, ipaddress, pathlib, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML requis : pip install pyyaml")

MARKERS = ["A_RENSEIGNER", "A_VERIFIER", "A_CONFIRMER_MICK", "A_CONFIRMER_GLOBAL", "HORS_PERIMETRE_PRODUIT"]
MARK_RE = re.compile(r"#\s*\[(%s)\]\s*(.*)$" % "|".join(MARKERS))
FIELD_RE = re.compile(r"Quoi\s*:\s*(?P<quoi>[^|]*)\|\s*Pourquoi\s*:\s*(?P<pourquoi>[^|]*)\|\s*Qui\s*:\s*(?P<qui>[^|]*)\|\s*Où\s*:\s*(?P<ou>[^|]*)\|\s*Bloquant\s*:\s*(?P<bloq>oui|non)")
PATTERNS = {"P1", "P2", "P3", "P4", "P5", "P6", "P7"}
PROPOSED_PATTERNS = {"P7"}
REQUIRED = ["schemaVersion", "dataProduct", "environments", "privatisation", "flows", "dependencies", "security", "extensions", "traceability"]
ENVS = ["DEV", "ITG", "PPR", "PRD"]
SECRET_RE = re.compile(r"(client[_-]?secret|password|sharedkey|accountkey)\s*:\s*(?!null)\S+", re.I)
IP_RE = re.compile(r"\b(\d{1,3}\.){3}\d{1,3}(/\d{1,2})?\b")


def yaml_path_of_line(lines, idx):
    """Chemin YAML approximatif d’une ligne (pour le rapport)."""
    path, indent = [], len(lines[idx]) - len(lines[idx].lstrip())
    m = re.match(r"\s*-?\s*([\w.-]+)\s*:", lines[idx])
    if m:
        path.append(m.group(1))
    for j in range(idx - 1, -1, -1):
        s = lines[j]
        if not s.strip() or s.lstrip().startswith("#"):
            continue
        ind = len(s) - len(s.lstrip())
        if ind < indent:
            m = re.match(r"\s*-?\s*([\w.-]+)\s*:", s)
            if m:
                path.insert(0, m.group(1))
            indent = ind
            if ind == 0:
                break
    return ".".join(path)


def scan_markers(text):
    out, lines = [], text.splitlines()
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") and not re.match(r"\s+#", line) and i < 20:
            continue  # en-tête du fichier
        m = MARK_RE.search(line)
        if not m:
            continue
        f = FIELD_RE.search(m.group(2))
        out.append({"line": i + 1, "marker": m.group(1), "path": yaml_path_of_line(lines, i) if not line.lstrip().startswith("#") else "(commentaire)",
                    "quoi": f["quoi"].strip() if f else m.group(2).strip(), "pourquoi": f["pourquoi"].strip() if f else "",
                    "qui": f["qui"].strip() if f else "", "ou": f["ou"].strip() if f else "",
                    "bloquant": (f["bloq"] == "oui") if f else False})
    return out


def check_security(text):
    issues = []
    for i, line in enumerate(text.splitlines(), 1):
        code = line.split("#", 1)[0]
        if SECRET_RE.search(code):
            issues.append(f"ligne {i} : valeur ressemblant à un secret")
        for m in IP_RE.finditer(code):
            try:
                ipaddress.ip_network(m.group(0), strict=False)
                issues.append(f"ligne {i} : adresse IP dans un manifeste ({m.group(0)}) — elle appartient à la configuration centrale")
            except ValueError:
                pass
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent))
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    root = pathlib.Path(a.root)
    files = sorted(p for p in (root / "manifests").rglob("*.yml") if "templates" not in p.parts)
    sp_file, kv_file = root / "inventory/service-principals.yml", root / "inventory/keyvault-references.yml"
    sp_ids = set((yaml.safe_load(sp_file.read_text(encoding="utf-8")) or {}).get("servicePrincipals", {})) if sp_file.exists() else set()
    kv_doc = yaml.safe_load(kv_file.read_text(encoding="utf-8")) if kv_file.exists() else {}

    docs, errors = {}, []
    for p in files:
        text = p.read_text(encoding="utf-8")
        try:
            d = yaml.safe_load(text)
        except yaml.YAMLError as e:
            errors.append(f"{p.relative_to(root)} : YAML invalide ({e})")
            continue
        miss = [k for k in REQUIRED if k not in d]
        if miss:
            errors.append(f"{p.relative_to(root)} : champs absents {miss}")
        docs[d["dataProduct"]["id"]] = {"path": p, "doc": d, "markers": scan_markers(text), "security": check_security(text), "refs": []}

    known = set(docs) | {"adp-opendata"}
    tracking_only = {"adp-opendata"}
    inbound = {k: [] for k in docs}
    for k, v in docs.items():
        d = v["doc"]
        for env in ENVS:
            if env not in d["environments"]:
                v["refs"].append(f"environnement {env} absent")
        ref = d["security"].get("identityRef", "")
        if ref and not ref.replace("<ENV>", "dev") in sp_ids:
            v["refs"].append(f"identityRef « {ref} » introuvable dans service-principals.yml")
        kvref = str(d["security"].get("keyVaultRefs", ""))
        if "#" in kvref and kvref.split("#")[1] not in (kv_doc or {}):
            v["refs"].append(f"keyVaultRefs « {kvref} » introuvable")
        for f in d.get("flows") or []:
            if f.get("pattern") not in PATTERNS:
                v["refs"].append(f"{f.get('id')} : pattern inconnu {f.get('pattern')}")
            if f.get("ruleCarriedBy") != k:
                v["refs"].append(f"{f.get('id')} : flux déclaré dans un manifeste qui ne porte pas la règle")
            tgt = f.get("target")
            if re.fullmatch(r"(adp|bdp|ucs)-[\w-]+|framework-items", str(tgt)):
                if tgt not in known:
                    v["refs"].append(f"{f.get('id')} : cible « {tgt} » sans manifeste ni suivi")
                elif tgt in tracking_only:
                    v["refs"].append(f"{f.get('id')} : cible « {tgt} » suivie hors manifeste actif (à confirmer)")
                if tgt in inbound and f.get("pattern") in {"P4", "P7"}:
                    inbound[tgt].append((k, f.get("pattern"), f.get("id")))
                elif tgt in inbound:
                    inbound[tgt].append((k, f.get("pattern"), f.get("id")))

    rows = []
    for k, v in docs.items():
        blocking = [m for m in v["markers"] if m["bloquant"]]
        v["deployable"] = not blocking and not v["security"] and not errors and not any("introuvable" in r for r in v["refs"])
        for m in v["markers"]:
            rows.append([k, str(v["path"].relative_to(root)), m["line"], m["path"], m["marker"], m["quoi"], m["pourquoi"], m["qui"], m["ou"], "oui" if m["bloquant"] else "non"])

    # --- sorties
    doc_dir, trk = root / "documentation", root / "tracking"
    doc_dir.mkdir(exist_ok=True); trk.mkdir(exist_ok=True)
    with open(trk / "missing-parameters.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["data_product", "fichier", "ligne", "champ", "marqueur", "quoi", "pourquoi", "qui", "ou", "bloquant"])
        w.writerows(rows)

    md = ["# Rapport de validation des manifestes", "",
          "> Schéma **proposé** par l’équipe produit (`dp-fabric-manifest/0.2-proposition`) — ce n’est pas le schéma officiel de Mick.", "",
          "Légende : 🔴 bloquant · 🟠 à confirmer · ⚪ hors périmètre produit · 🟢 aucun manque", "",
          "| Data product | Déployable | Bloquants | À confirmer | Hors périmètre | Contrôles de référence | Sécurité |",
          "|---|---|---|---|---|---|---|"]
    for k, v in docs.items():
        ms = v["markers"]
        nb = sum(m["bloquant"] for m in ms)
        nc = sum((not m["bloquant"]) and m["marker"] != "HORS_PERIMETRE_PRODUIT" for m in ms)
        nh = sum(m["marker"] == "HORS_PERIMETRE_PRODUIT" for m in ms)
        md.append(f"| `{k}` | {'🟢 oui' if v['deployable'] else '🔴 **non**'} | 🔴 {nb} | 🟠 {nc} | ⚪ {nh} | {len(v['refs'])} remarque(s) | {'🟢 OK' if not v['security'] else '🔴 ' + str(len(v['security']))} |")
    md += ["", "## Approbations entrantes calculées", "", "Chaque ligne est une approbation ou une règle à prévoir côté **cible** ; elle n’est déclarée qu’une fois (manifeste de la source).", ""]
    for k, lst in inbound.items():
        if lst:
            md.append(f"- **{k}** : " + ", ".join(f"{s} ({p})" for s, p, _ in sorted(set(lst))))
    md += ["", "## Remarques de référence", ""]
    for k, v in docs.items():
        for r in v["refs"]:
            md.append(f"- `{k}` — {r}")
    for e in errors:
        md.append(f"- ❌ {e}")
    md += ["", "## Détail des manques bloquants", "", "| Data product | Ligne | Champ | Marqueur | Quoi | Qui |", "|---|---|---|---|---|---|"]
    for r in rows:
        if r[9] == "oui":
            md.append(f"| `{r[0]}` | {r[2]} | `{r[3]}` | 🔴 {r[4]} | {r[5]} | {r[7]} |")
    (doc_dir / "manifest-validation-report.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    color = {"oui": "#f8d7da", "A_CONFIRMER_MICK": "#ffe5b4", "A_CONFIRMER_GLOBAL": "#ffe5b4", "A_VERIFIER": "#ffe5b4", "A_RENSEIGNER": "#ffe5b4", "HORS_PERIMETRE_PRODUIT": "#e2e3e5"}
    h = ["<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Validation des manifestes</title>",
         "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:24px;color:#1b1b1b}table{border-collapse:collapse;width:100%;font-size:13px;margin-bottom:24px}"
         "th,td{border:1px solid #ccc;padding:4px 6px;vertical-align:top}th{background:#00338d;color:#fff;text-align:left}"
         ".ko{color:#b00020;font-weight:600}.ok{color:#0a7d32;font-weight:600}</style></head><body>",
         "<h1>Validation des manifestes</h1><p><b>Schéma proposé</b> par l’équipe produit — ce n’est pas le schéma officiel de Mick.</p>",
         "<p>Rouge : manquant et bloquant · Orange : à confirmer · Gris : hors périmètre produit · Vert : validé</p>",
         "<table><tr><th>Data product</th><th>Déployable</th><th>Bloquants</th><th>Non bloquants</th></tr>"]
    for k, v in docs.items():
        nb = sum(m["bloquant"] for m in v["markers"])
        h.append(f"<tr><td>{k}</td><td class='{'ok' if v['deployable'] else 'ko'}'>{'oui' if v['deployable'] else 'non'}</td><td style='background:#f8d7da'>{nb}</td><td>{len(v['markers']) - nb}</td></tr>")
    h.append("</table><h2>Paramètres manquants</h2><table><tr><th>Data product</th><th>Ligne</th><th>Champ</th><th>Marqueur</th><th>Quoi</th><th>Pourquoi</th><th>Qui</th><th>Où</th><th>Bloquant</th></tr>")
    for r in rows:
        bg = color["oui"] if r[9] == "oui" else color.get(r[4], "#fff")
        h.append("<tr style='background:%s'>" % bg + "".join(f"<td>{html.escape(str(c))}</td>" for c in r[0:1] + r[2:]) + "</tr>")
    h.append("</table></body></html>")
    (doc_dir / "manifest-validation-report.html").write_text("\n".join(h), encoding="utf-8")

    for k, v in docs.items():
        print(f"{k:32} deployable={'oui' if v['deployable'] else 'non':3}  marqueurs={len(v['markers']):3}  bloquants={sum(m['bloquant'] for m in v['markers']):3}  remarques={len(v['refs'])}")
    if errors:
        print("\n".join(errors)); return 1
    if a.strict and not all(v["deployable"] for v in docs.values()):
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
