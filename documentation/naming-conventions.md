# Conventions de nommage DEV → ITG → PPR → PRD (T8)

Une matrice, pas une substitution : seul un nom confirmé dans une source pour un environnement est considéré comme connu.

## 1. Décomposition des noms DEV observés

| Ressource | Exemple DEV | Structure constatée | Remarque |
|---|---|---|---|
| Workspace Fabric | `FR - DP - DEV - FAB - ADP - MDS - MANAGED` | `FR - DP - <ENV> - FAB - <ADP\|BDP> - <Nom> - MANAGED` | tiret simple ; UCS en « Managed » |
| Workspace Power BI | `FR - DP - DEV - PBI - UCS - Reporting Fees & WIP - SelfBuild` | `… - PBI - UCS - <Nom> - Self{Build,Test,Use}` | |
| Capacité | `frfrfcdevdp0001` | `frfr` + `fc` + `<env>` + `dp` + `0001` | PRD : `frfrfcprddp0001` confirmé |
| Resource group | `frappdevdp0001` | `fr` + `app` + `<env>` + `dp` + `0001` | |
| VNet | `fralzvnetdev1055` | `fr` + `alz` + `vnet` + `<env>` + n° | numéro attribué par le Global |
| Route table | `fr_rt_fralzvnetdev1055` | `fr_rt_` + VNet | |
| Key Vault | `frfrkvdevdp0001` | `frfr` + `kv` + `<env>` + `dp` + `0001` | coffre unique tous environnements |
| Private Endpoint workspace | `FRFRAPEFWDEVDPADPMDSMANAGED0001-1` | `FRFRAPEFW` + `<ENV>` + `DP` + `<TOKEN>` + `MANAGED0001-<n>` | `-1` entrant |
| MPE | `FRFRAPEFWDEVDPADPMDSMANAGED0001-6` | nom de la cible + suffixe | compteur par cible |
| Private Link service | `frfrpldevdpadpmdsmanaged0001` | `frfrpl` + `<env>` + `dp` + `<token>` + `managed0001` | **contradiction C4** |
| Connexion | `MDS_DEV_DP_FABRIC` | `<OBJET>_<ENV>_DP_FABRIC` | |
| SPN | `FR-DEV-Data Platform-RITM6601337` | `FR-<DEV\|QA\|STAG\|PROD>-Data Platform-<RITM>` | libellés Global ≠ codes ENV |

## 2. Matrice par environnement

| Ressource | DEV | ITG | PPR | PRD |
|---|---|---|---|---|
| Workspaces | CONFIRMÉ | CONFIRMÉ (doc 1) | CONFIRMÉ | CONFIRMÉ |
| Capacité | frfrfcdevdp0001 | 🔴 contradiction C1 | 🔴 contradiction C1 | frfrfcprddp0001 (ID manquant) |
| Souscription | FR-AZR-DP-DEV | 🔴 manquant | 🔴 manquant | 🔴 manquant |
| Resource group | frappdevdp0001 | frappitgdp0001 | frapppprdp0001 | frappprddp0001 |
| VNet | fralzvnetdev1055 | fralzvnetitg1055 | fralzvnetppr1055 | fralzvnetprd1055 |
| Subnet | snet-kpmg-backend | snet-kpmg-backend | snet-kpmg-backend | snet-kpmg-backend |
| Route table | fr_rt_fralzvnetdev1055 | fr_rt_fralzvnetitg1055 | fr_rt_fralzvnetppr1055 | fr_rt_fralzvnetprd1055 |
| Key Vault | frfrkvdevdp0001 | même coffre (décision 22/10) | même coffre | même coffre |
| Private Endpoint | `FRFRAPEFWDEVDP<TOKEN>MANAGED0001-1` | `FRFRAPEFWITGDP<TOKEN>MANAGED0001-1` | `FRFRAPEFWPPRDP<TOKEN>MANAGED0001-1` | `FRFRAPEFWPRDDP<TOKEN>MANAGED0001-1` |
| Private Link | `frfrpldevdp<token>managed0001` (confirmé) | `frfrplitgdp<token>managed0001` | `frfrplpprdp<token>managed0001` | `frfrplprddp<token>managed0001` |
| MPE | `FRFRAPEFWDEVDP<CIBLE>MANAGED0001-<n>` | `FRFRAPEFWITGDP<CIBLE>MANAGED0001-<n>` | `FRFRAPEFWPPRDP<CIBLE>MANAGED0001-<n>` | `FRFRAPEFWPRDDP<CIBLE>MANAGED0001-<n>` |
| SPN | FR-DEV-… | FR-QA-… | FR-STAG-… | FR-PROD-… |
| Connexions | `<OBJET>_DEV_DP_FABRIC` | `<OBJET>_ITG_DP_FABRIC` (convention) | idem | idem |

**Règle (décision du 08/11/2026)** : les noms du Private Endpoint, du Private Link et des MPE en ITG, PPR et PRD reprennent la nomenclature DEV, en remplaçant seulement le code d’environnement (`DEV` → `ITG`, `PPR`, `PRD` ; en minuscules pour le Private Link). Le jeton du data product est identique dans les 4 environnements (Performance Engagement garde `BDPPERFORMANCEFINANCIERE`). Pour les data products sans ressource DEV, le jeton suit la même règle : catégorie + nom en majuscules, sans espace ni accent (`ADPSIRENE`, `BDPCOMPTEENGAGE`, `BDPOPPORTUNITE`, `BDPCONTACT`, `BDPLEAD`, `BDPCAMPAIGN`). Les noms figurent dans `plannedResources` de chaque manifeste. La même règle s’applique au resource group, au VNet, au subnet et à la route table (`frapp<env>dp0001`, `fralzvnet<env>1055`, `snet-kpmg-backend`, `fr_rt_fralzvnet<env>1055`), le numéro 1055 du VNet étant repris tel quel. Restent au Global : souscription, plage IP, DNS et peering.

## 3. ADP Référentiel

| Env. | Workspace | ID |
|---|---|---|
| DEV | FR - DP - DEV - FAB - ADP - Referentiel - MANAGED | 4c6b33a2-d61c-4c92-8cea-80eadcf277d2 |
| ITG | FR - DP - ITG - FAB - ADP - Referentiel - MANAGED | 13b7d0a0-4ff3-4dca-a3d2-e15974b614e7 |
| PPR | FR - DP - PPR - FAB - ADP - Referentiel - MANAGED | 161b78a6-bded-43c1-97fd-96e7aec40a2e |
| PRD | FR - DP - PRD - FAB - ADP - Referentiel - MANAGED | ba74b427-a836-4686-a195-252f747d867e |

Source : `config.yml` et `dependencies.yml` du dépôt its-dp-fab-adp-referentiel-managed (03/11/2026). Ressources DEV : PE `FRFRAPEFWDEVDPADPREFERENTIELMANAGED0001-1`, Private Link `frfrpldevdpadpreferentielmanaged0001` (à vérifier, C4), MPE `FRFRAPEFWDEVDPADPREFERENTIELMANAGED0001-<n>`. Pipeline CI `its-dp-fab-adp-referentiel-managed-CI`, projet SonarQube `Discovery_DP-FAB-ADP-Referentiel-Managed`.

## 4. Data products ajoutés le 08/11/2026

| Dépôt | Workspace (`<ENV>` = DEV, ITG, PPR, PRD) |
|---|---|
| its-dp-fab-adp-sirene-managed | FR - DP - <ENV> - FAB - ADP - Sirene - MANAGED |
| its-dp-fab-bdp-compte-engage-managed | FR - DP - <ENV> - FAB - BDP - Compte Engage - MANAGED |
| its-dp-fab-bdp-opportunite-managed | FR - DP - <ENV> - FAB - BDP - Opportunite - MANAGED |
| its-dp-fab-bdp-contact-managed | FR - DP - <ENV> - FAB - BDP - Contact - MANAGED |
| its-dp-fab-bdp-lead-managed | FR - DP - <ENV> - FAB - BDP - Lead - MANAGED |
| its-dp-fab-bdp-campaign-managed | FR - DP - <ENV> - FAB - BDP - Campaign - MANAGED |
| its-dp-fab-adp-gds-managed | FR - DP - <ENV> - FAB - ADP - GDS - MANAGED (noms et ID communiqués le 08/11/2026 pour les 4 environnements) |
| its-dp-fab-adp-opendata-managed | FR - DP - <ENV> - FAB - ADP - OPENDATA - MANAGED — **non privatisé** (données open source) |

Noms sans accent (« Compte Engage », « Opportunite ») et tiret simple, comme communiqués. Aucun PE en DEV : le jeton de leurs ressources Azure (`FRFRAPEFWDEVDP<TOKEN>MANAGED0001-1`) reste à fixer avec Mick.

## 5. Gateways et connexions

| Objet | Nom relevé | Structure |
|---|---|---|
| Gateway | DP-FABRIC-GW-HORS-PROD, DP-FABRIC-GW-PROD | `DP-FABRIC-GW-<HORS-PROD\|PROD>` |
| Gateway | Gateway_prod | hors convention (contact BI) |
| Connexion SQL | MDS_DEV_DP_FABRIC, STAGING_DEV_DP_FABRIC | `<OBJET>_<ENV>_DP_FABRIC` (confirmée en DEV) |
| Connexion Fabric Data Pipelines | DP-Fabric-Global-APR | nom unique, sans environnement |

## 6. Points à arbitrer

1. Code d’environnement des ressources réseau : tranché (ITG, PPR, PRD, nomenclature DEV).
2. Convention des Private Link services : confirmée par l’inventaire des ressources DEV (C4 résolu).
3. Performance Engagement (C6, résolu) : le workspace a été renommé depuis « Performance Financière » ; les ressources gardent le jeton `PERFORMANCEFINANCIERE`, y compris en ITG, PPR et PRD (nomenclature DEV).
4. Casse « Managed » du UCS (C15).
