# Procédure d’inventaire en lecture seule (T3)

## 1. Prérequis

- Compte personnel avec rôle **Reader** sur FR-AZR-DP-DEV et rôle **Viewer** (ou plus) sur les workspaces Fabric.
- `az` CLI, `jq`, Python 3 avec PyYAML.
- Aucune identité de pipeline : l’inventaire se fait avec la session de l’utilisateur.

## 2. Exécution

```bash
az login
./scripts/inventory-dev-azure.sh ./_inventaire/azure
python3 scripts/inventory-dev-fabric.py --env DEV --out ./_inventaire/fabric-dev
python3 scripts/inventory-dev-fabric.py --env ITG --out ./_inventaire/fabric-itg   # ID ITG/PPR/PRD déjà confirmés : contrôle de cohérence uniquement
# Référentiel : CICD/ref_dynamique/02_fab_cli.py --env ITG|PPR|PRD (dépôt its-dp-fab-adp-referentiel-managed) relève les ID complets
```

Les chemins d’API Fabric du réseau (`/networking/communicationPolicy…`) sont à vérifier dans la documentation Microsoft à la date d’exécution : un endpoint indisponible est consigné comme erreur, sans interrompre l’inventaire.

## 3. Garanties

| Garantie | Mécanisme |
|---|---|
| Lecture seule Azure | fonction `run()` qui refuse toute sous-commande autre que `list`, `show`, `get` |
| Aucun secret lu | `keyvault secret list` (métadonnées), refus de `secret show` |
| Lecture seule Fabric | méthode HTTP `GET` uniquement |
| Assainissement | suppression des clés `value`, `secret`, `password`, `connectionString`… dans les JSON |
| Jeton | jamais écrit sur disque ni affiché |

## 4. Contrôle et comparaison

1. Vérifier `summary.txt` : nombre de PE (16 dans le périmètre), d’IP (85 dans le périmètre) — toute ressource supplémentaire est signalée comme hors périmètre, statut des connexions (Approved).
1 bis. Zone DNS : 86 recordsets et 1 lien VNet attendus ; comparer les enregistrements A avec `inventory/dns-records-dev.csv` (79 dans le périmètre). Le droit Reader sur fr-connectivity peut manquer : l’échec est consigné sans arrêter l’inventaire.
2. Comparer les ID des workspaces avec `inventory/workspaces-by-environment.csv` ; tout écart passe la valeur du manifeste en `[A_VERIFIER]`.
3. Comparer les MPE exportés avec `inventory/managed-private-endpoints-dev.csv`.
4. Relancer `python3 scripts/validate-manifests.py`.
5. Ne jamais committer les dossiers `_inventaire/` bruts : seuls les extraits assainis entrent dans `inventory/`.
