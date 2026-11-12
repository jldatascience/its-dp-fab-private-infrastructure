# Reprise de l’existant par Terraform (T13)

> Aucune commande `terraform import`, `apply` ou `destroy` n’est exécutée par ce lot. Ce document décrit la procédure à valider avec Mick.

## 1. Situation

| Environnement | État constaté | Mode proposé |
|---|---|---|
| DEV | 15 workspaces privatisés à la main, 16 PE, 75 lignes MPE | **import** (ou documentation seule si DEV reste hors Terraform — à décider) |
| ITG, PPR | workspaces existants (ID à vérifier), privatisation inconnue | inventaire, puis création des ressources réseau par Terraform |
| PRD | idem ; capacité gomfcaprodeuwfabricdataplatformfr0001 | idem, après validation en PPR |

## 2. Procédure

1. **Inventaire** : `scripts/inventory-dev-azure.sh` et `scripts/inventory-dev-fabric.py --env <ENV>` (lecture seule).
2. **Rapprochement** : compléter `environments.<ENV>.existingResources` du manifeste avec les ID exportés.
3. **Blocs `import` déclaratifs** dans le code de Mick (Terraform ≥ 1.5), revus en pull request ; jamais de commande `terraform import` manuelle.
4. **`terraform plan` uniquement**, sortie archivée ; critère d’acceptation : **0 destruction, 0 remplacement**, seules des mises à jour de tags acceptées.
5. Si le plan propose un remplacement : corriger le code (nom, propriété) ; ne jamais forcer.
6. Validation par Mick et par la sécurité, puis `apply` par le pipeline.
7. Garde-fous : `lifecycle { prevent_destroy = true }` sur Private Endpoint et Private Link ; verrou Azure `CanNotDelete` sur le RG (décision Global).

## 3. Identifiants d’import (à confirmer dans la documentation des providers)

| Ressource | Identifiant attendu | Source de la valeur |
|---|---|---|
| Private Endpoint | ID ARM `/subscriptions/…/resourceGroups/frappdevdp0001/providers/Microsoft.Network/privateEndpoints/<nom>` | export VNet |
| Private Link service Fabric (azapi) | ID ARM `…/providers/Microsoft.Fabric/privateLinkServicesForFabric/<nom>` | `az resource list` (C4) |
| Politique de communication | ID du workspace | inventaire Fabric |
| Règles sortantes | ID du workspace | inventaire Fabric |
| MPE | ID du workspace + ID du MPE | inventaire Fabric |

## 4. Cas du Référentiel

1. DEV : workspace déjà privatisé (PE `FRFRAPEFWDEVDPADPREFERENTIELMANAGED0001-1`, 5 IP, DNS) → import.
2. Les 10 MPE entrants (Framework P4, BDP et UCS P7, workspaces personnels) sont « À créer » : création par Terraform, puis approbation par le propriétaire du Référentiel.
3. ITG, PPR, PRD : les workspaces existent (ID ITG 13b7d0a0-4ff3-…, PPR 161b78a6-bded-…, PRD ba74b427-a836-… communiqués le 08/11/2026) : privatiser sans recréer.
4. Le déploiement des items reste bloqué côté socle (`inventory_status: pending`, aucun item) : il est indépendant de la privatisation.

## 5. Zone DNS gérée par Terraform

La zone `privatelink.fabric.microsoft.com` porte le tag `Status: Managed by Terraform` (code de la connectivité, souscription fr-connectivity). La lire et en récupérer l’ID ne pose aucun problème ; toute écriture (enregistrements des nouveaux Private Endpoints) doit passer par ce processus ou être convenue avec lui, sinon elle sera écrasée ou créera de la dérive.

## 6. Dérive

- Un plan périodique (lecture seule) compare l’état réel au manifeste.
- Toute modification manuelle dans le portail est signalée, puis reportée dans le manifeste ou annulée par le pipeline.
- Les approbations de MPE (manuelles) ne sont pas une dérive : elles sont suivies dans le classeur.
