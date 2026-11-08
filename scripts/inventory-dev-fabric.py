#!/usr/bin/env python3
"""inventory-dev-fabric.py — inventaire Fabric d’un environnement, LECTURE SEULE.

N’émet QUE des requêtes HTTP GET vers l’API Fabric (api.fabric.microsoft.com/v1).
Aucune création, modification, suppression ou approbation. Aucun secret n’est lu :
le jeton est obtenu par « az account get-access-token » (session interactive de
l’utilisateur) et n’est jamais écrit sur disque ni affiché.

Usage :
  python3 inventory-dev-fabric.py --env DEV [--filter "FR - DP - DEV"] [--out dossier]

Collecte, pour chaque workspace dont le nom contient le filtre :
  - identité (id, nom, capacité) ;
  - politique de communication réseau (entrant / sortant) ;
  - règles sortantes (connexions cloud, gateways) et politique Git sortante ;
  - Managed Private Endpoints (nom, cible, statut d’approbation) ;
  - liste des items (type et nom uniquement) ;
  - attributions de rôles (principal et rôle, sans donnée personnelle superflue).
Les endpoints non disponibles pour le compte sont signalés et ignorés.
"""
import argparse, datetime, json, pathlib, subprocess, sys, urllib.error, urllib.request

API = "https://api.fabric.microsoft.com/v1"
SENSITIVE = {"secret", "password", "clientsecret", "connectionstring", "key", "token", "credentials", "value"}


def token():
    try:
        r = subprocess.run(["az", "account", "get-access-token", "--resource", "https://api.fabric.microsoft.com",
                            "--query", "accessToken", "-o", "tsv"], capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        sys.exit(f"Impossible d’obtenir un jeton (az login requis) : {e}")
    return r.stdout.strip()


def get(path, tok):
    """GET uniquement. Gère la pagination continuationUri."""
    url, items = f"{API}{path}", []
    while url:
        req = urllib.request.Request(url, method="GET", headers={"Authorization": f"Bearer {tok}"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = json.loads(resp.read() or b"{}")
        except urllib.error.HTTPError as e:
            return {"_error": e.code, "_path": path}
        if "value" in body and isinstance(body["value"], list):
            items.extend(body["value"])
            url = body.get("continuationUri")
        else:
            return body
    return items


def sanitize(o):
    if isinstance(o, dict):
        return {k: ("<masqué>" if k.lower() in SENSITIVE and not isinstance(v, (list, dict)) else sanitize(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [sanitize(x) for x in o]
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True, choices=["DEV", "ITG", "PPR", "PRD"])
    ap.add_argument("--filter", default=None, help="sous-chaîne du nom (défaut : 'FR - DP - <ENV> -')")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    flt = a.filter or f"FR - DP - {a.env} -"
    out = pathlib.Path(a.out or f"inventory-fabric-{a.env.lower()}-{datetime.datetime.now():%Y%m%d-%H%M%S}")
    out.mkdir(parents=True, exist_ok=True)
    tok = token()

    wss = get("/workspaces", tok)
    if isinstance(wss, dict) and "_error" in wss:
        sys.exit(f"Lecture des workspaces refusée : HTTP {wss['_error']}")
    wss = [w for w in wss if flt in w.get("displayName", "")]
    result = {"generated": datetime.datetime.now().isoformat(timespec="seconds"), "environment": a.env, "filter": flt, "workspaces": []}
    for w in sorted(wss, key=lambda x: x["displayName"]):
        wid = w["id"]
        print(f"-> {w['displayName']} ({wid})")
        entry = {"id": wid, "displayName": w["displayName"], "capacityId": w.get("capacityId")}
        for key, path in [
            ("networkCommunicationPolicy", f"/workspaces/{wid}/networking/communicationPolicy"),
            ("outboundCloudConnectionRules", f"/workspaces/{wid}/networking/communicationPolicy/outbound/connections"),
            ("outboundGatewayRules", f"/workspaces/{wid}/networking/communicationPolicy/outbound/gateways"),
            ("gitOutboundPolicy", f"/workspaces/{wid}/networking/communicationPolicy/outbound/git"),
            ("managedPrivateEndpoints", f"/workspaces/{wid}/managedPrivateEndpoints"),
            ("roleAssignments", f"/workspaces/{wid}/roleAssignments"),
        ]:
            entry[key] = sanitize(get(path, tok))
        items = get(f"/workspaces/{wid}/items", tok)
        entry["items"] = [{"type": i.get("type"), "displayName": i.get("displayName")} for i in items] if isinstance(items, list) else items
        result["workspaces"].append(entry)

    (out / f"fabric-{a.env.lower()}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    with open(out / f"workspaces-{a.env.lower()}.csv", "w", encoding="utf-8-sig") as fh:
        fh.write("workspace;workspace_id;capacity_id;mpe;items\n")
        for e in result["workspaces"]:
            n_mpe = len(e["managedPrivateEndpoints"]) if isinstance(e["managedPrivateEndpoints"], list) else "?"
            n_it = len(e["items"]) if isinstance(e["items"], list) else "?"
            fh.write(f"{e['displayName']};{e['id']};{e['capacityId']};{n_mpe};{n_it}\n")
    print(f"Terminé : {out}")


if __name__ == "__main__":
    main()
