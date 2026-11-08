# Patterns de flux P1 à P6 (+ P7 proposé) (T10)

Définitions **exactes** de `Cartographie_Flux_Workspaces_Fabric.xlsx` v2 (onglet Patterns & actions). Le flux est déclaré dans le manifeste du workspace qui **porte la règle** ; le validateur calcule les approbations côté cible.

| Pattern | Cas | Action technique | Workspace portant la règle | Approbation |
|---|---|---|---|---|
| **P1** | accès on-premise via la gateway (Framework) | Gateway Connection Policy | workspace qui exécute la copie (Framework) | Data Platform, administrateurs de la gateway |
| **P2** | Invoke Pipeline **data product → Framework** | Data Connection Rule « Fabric Data Pipelines » | data product appelant | administrateur du workspace |
| **P3** | Invoke Pipeline **Framework → data product** | Data Connection Rule « Fabric Data Pipelines » | Framework | administrateur du workspace |
| **P4** | notebook Spark écrivant d’un workspace à l’autre | Managed Private Endpoint du Framework vers le data product cible | Framework | **propriétaire du workspace cible** (manuelle) |
| **P5** | appel d’API REST | Web Activity + Data Connection Rule REST | workspace appelant | sécurité (URL autorisée) |
| **P6** | synchronisation Git | Git outbound policy | workspaces synchronisés avec Git (**DEV uniquement**) | administrateur du workspace |
| **P7** *(PROPOSÉ)* | lecture inter-data products (BDP/UCS → ADP/BDP) | Managed Private Endpoint de la source vers la cible | consommateur | propriétaire du workspace cible |

> **Correction** : nos livrables précédents (manifeste MDS, dossier d’atelier) notaient MDS → Framework en P3. La définition correcte est **P2**. P3 désigne le sens Framework → data product.

## Application par catégorie

| Source → cible | Pattern | Source de la règle |
|---|---|---|
| ADP → Framework | P2 | matrice (DEV confirmé ; ITG/PPR « ? ») |
| BDP → Framework | P2 (à vérifier) | BDP absents de la matrice |
| Framework → ADP | P1, P3, P4 | matrice |
| Framework → BDP | P4 | MPE DEV |
| BDP/UCS → ADP/BDP | P7 (proposé) | 75 MPE DEV, liste des interconnexions |
| Framework → API Fabric | P5 | décision du 29/10/2026 (référencement dynamique), non configuré en DEV |
| Tous (DEV) → Git | P6 | diagonale de la matrice |

## Mutualisé ou par workspace

| Composant | Portée |
|---|---|
| VNet, subnet, route table, peering, DNS | **mutualisé par environnement** (Global / Mick) |
| Private Link service, Private Endpoint, enregistrements DNS | **par workspace** |
| Politique entrante/sortante, DCR, Git outbound | **paramètre Fabric du workspace** |
| Gateway Connection Policy, connexions | **par connexion** |
| MPE | **par couple source → cible** |

Les flux entièrement internes à Fabric n’ouvrent pas de règle sur le firewall du hub (à confirmer : port et protocole laissés à `null` avec `[A_VERIFIER]`).
