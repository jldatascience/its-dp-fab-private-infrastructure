# Sources, classification des valeurs et contradictions (T1)

Analyse du 08/11/2026. Chaque valeur utilisée dans les manifestes porte l’un des statuts suivants.

| Statut | Signification | Rendu |
|---|---|---|
| **CONFIRMÉ** | lu dans une pièce jointe (source citée) | valeur renseignée, commentaire `# CONFIRMÉ (source)` |
| **À VÉRIFIER** | présent dans une source ancienne ou incohérente | valeur renseignée + `[A_VERIFIER]` |
| **MANQUANT** | aucune source | `null` + `[A_RENSEIGNER]` ou `[A_CONFIRMER_GLOBAL]` |
| **PROPOSÉ** | choix de conception de l’équipe produit, à valider | `[A_CONFIRMER_MICK]` |
| **HORS PÉRIMÈTRE PRODUIT** | fourni par la configuration centrale ou le Global | `null` + `[HORS_PERIMETRE_PRODUIT]` |

## 0. Dépôt ADP Référentiel (03/11/2026)

Le dépôt `its-dp-fab-adp-referentiel-managed` (README, CHANGELOG et `CICD/` du 03/11/2026) apporte :
- les noms des workspaces `FR - DP - <ENV> - FAB - ADP - Referentiel - MANAGED` pour DEV, ITG, PPR et PRD (confirmés le 03/11/2026, tiret simple) ;
- les préfixes des ID des workspaces ITG (`13b7d0a0-`), PPR (`161b78a6-`) et PRD (`ba74b427-`) dans `guid_policy.forbidden_prefixes` ; les ID complets ont été communiqués le 08/11/2026 ;
- l’état du dépôt : aucun item Fabric (`fabric/.gitkeep`), `inventory_status: pending`, Git Integration DEV non connectée ;
- le Framework comme unique prérequis de déploiement, `framework.items`, `connections`, `variable_libraries` et `data_dependencies` vides, à relever ;
- le coffre unique `frfrkvdevdp0001` et 3 service connections ARM ITG, PPR, PRD à créer en fédération d’identité ;
- l’outillage de référencement dynamique `CICD/ref_dynamique/01` à `04`, en lecture seule, réutilisable pour relever les ID (`02_fab_cli.py --env <ENV>`).

## 1. Pièces jointes analysées

| # | Pièce | Apport principal |
|---|---|---|
| 1 | doc 1 — liste des workspaces | noms des workspaces des 4 environnements, workspaces Power BI du UCS, workspaces personnels DEV, mail de Daniels sur les risques CI/CD |
| 2 | doc 2 / doc 3 — contenu des dépôts | 11 dépôts, anciens `deploy.py` (ID de workspaces ITG/PPR/PRD, capacités, client ID des SPN) |
| 3 | Liste des interconnexions | dépendances de données entre data products (01 à 17) |
| 4 | Cartographie_Flux_Workspaces_Fabric.xlsx | définitions P1 à P6, matrice source × cible |
| 5 | Resource group frappdevdp0001 | location, tags |
| 6 | Configuration JSON du VNet | VNet, subnet, route table, peering, 85 ipConfigurations dans le périmètre |
| 7 | Informations du VNet | plage, DNS |
| 8 | Modèle ARM | type `Microsoft.Fabric/privateLinkServicesForFabric`, API 2024-06-01 |
| 9 | DAG DMND0003667 Finance x CDG | architecture cible par Data Domain (≠ existant) |
| 10 | Listing record_set par workspace (VF) | 79 enregistrements DNS dans le périmètre, FQDN contenant les ID de workspaces |
| 11 | PE managed listing (VF) | 19 Private Link, 75 MPE avec statut (périmètre) |
| 12 | Service principal par environnement | 4 SPN, n° RITM |
| 13 | Key vault frfrkvdevdp0001 | configuration, noms des secrets et expirations |
| 15 | Dépôt its-dp-fab-adp-referentiel-managed : README, CHANGELOG, config.yml, dependencies.yml, parameter.yml, CI.yml, CD.yml, PR-Validation.yml, scripts ref_dynamique 01 à 04 | noms des workspaces Référentiel, préfixes des ID ITG/PPR/PRD, état du dépôt, identités |
| 16 | Liste des dépôts et workspaces communiquée le 08/11/2026 | 7 dépôts (adp-opendata, adp-sirene, bdp-compte-engage, bdp-opportunite, bdp-contact, bdp-lead, bdp-campaign) et 24 workspaces Sirene, Compte Engage, Opportunite, Contact, Lead, Campaign (DEV, ITG, PPR, PRD) |
| 17 | Dépôt its-dp-fab-adp-opendata-managed : README, CHANGELOG, config.yml, dependencies.yml, parameter.yml, CI.yml, CD.yml, PR-Validation.yml, scripts ref_dynamique 01 à 04 (01/11/2026) | workspaces OPENDATA des 4 environnements, préfixe de l’ID DEV `99adda55-`, pipeline CI `its-dp-fab-opendata-managed-CI`, dépôt sans item |
| 18 | Liste des gateways utilisées (Recap_connexions_gateway_Fabric : onglets Gateways et Connexions) | 3 gateways (DP-FABRIC-GW-HORS-PROD, DP-FABRIC-GW-PROD, Gateway_prod), 3 connexions DEV (DP-Fabric-Global-APR, STAGING_DEV_DP_FABRIC, MDS_DEV_DP_FABRIC) |
| 19 | Export JSON complet du Key Vault frfrkvdevdp0001 + capture des secrets | access policies vides, aucune règle IP/VNet, connexion PE approuvée, 12 secrets Enabled |
| 20 | Fiche « ID de la zone DNS privée à utiliser » | ID complet de la zone privatelink.fabric.microsoft.com (souscription fr-connectivity), 86 recordsets, 1 lien VNet, gérée par Terraform |
| 21 | Captures « Edit subnet » snet-kpmg-backend | private subnet, aucun NAT, NSG, service endpoint ni délégation ; route table ; PE network policy Disabled |
| 23 | Inventaire_ressources_Azure_Fabric (onglet Ressources) | noms réels des 15 Private Link, des Private Endpoints et de leurs NIC (`…-1-nic`), route table, VNet, capacité, Key Vault et NIC du PE Key Vault |
| 22 | Indications du 08/11/2026 | dépôt ADP GDS `its-dp-fab-adp-gds-managed` ; noms et ID des workspaces GDS DEV (69943001-…), ITG (071742c7-…), PPR (87241b71-…), PRD (55038f5c-…) ; OPENDATA non privatisé (données open source) |
| 14 | Captures (souscription, capacités, interconnexions) | souscription FR-AZR-DP-DEV, capacités F16 / F32 |

## 2. Valeurs confirmées (extrait)

| Domaine | Valeur | Source |
|---|---|---|
| Tenant | deff24bb-2089-4400-8c8e-f71e680378b2 | capture souscription |
| Souscription DEV | FR-AZR-DP-DEV — 0c53c37e-2ed2-4d58-b147-8f80763294ce | capture |
| Resource group | frappdevdp0001 (francecentral) | export |
| VNet | fralzvnetdev1055 — 172.23.20.0/24 — westeurope — DNS 10.113.192.100 | JSON VNet |
| Subnet | snet-kpmg-backend — 172.23.20.0/24 — sans NSG ni NAT — route table fr_rt_fralzvnetdev1055 | JSON VNet |
| Peering | vers fralzvnet0001 (10.113.192.0/22, RG frinfalzconnectivityhub0001, souscription 1fe4e122-…) | JSON VNet |
| Private Endpoints | 16 (15 workspaces + Key Vault), 85 IP | JSON VNet |
| Key Vault | frfrkvdevdp0001 — Premium, RBAC, purge protection, Deny | export |
| SPN | 4 (DEV, QA, STAG, PROD) avec Application ID | listing SPN |
| Capacité DEV | frfrfcdevdp0001, F16 | capture |
| ID des workspaces DEV | 14 ID dérivés des FQDN DNS | listing DNS |
| ID des workspaces ITG / PPR / PRD (30) | MDS, IBS, 6 BDP, Framework, UCS | anciens `deploy.py`, exactitude confirmée le 08/11/2026 |
| ID des workspaces GDS (4 environnements) | DEV 69943001-…, ITG 071742c7-…, PPR 87241b71-…, PRD 55038f5c-… | communiqués le 08/11/2026 |
| ID des workspaces Référentiel | DEV 4c6b33a2-…, ITG 13b7d0a0-4ff3-4dca-a3d2-e15974b614e7, PPR 161b78a6-bded-43c1-97fd-96e7aec40a2e, PRD ba74b427-a836-4686-a195-252f747d867e | communiqués le 08/11/2026 |
| Workspaces Référentiel | `FR - DP - <ENV> - FAB - ADP - Referentiel - MANAGED` (4 env.) ; dépôt its-dp-fab-adp-referentiel-managed | README du dépôt |

## 3. Valeurs à vérifier

| Valeur | Raison |
|---|---|
| Noms des Private Link services | listing ≠ export ARM |
| État de privatisation ITG / PPR / PRD | aucune ressource réseau hors DEV dans les exports |
| Protocoles et ports des flux | non précisés dans la cartographie |
| P2 des BDP vers le Framework | BDP absents de la matrice |

## 4. Valeurs manquantes (bloquantes pour ITG)

souscription, resource group, VNet, subnet, plage IP, DNS et peering d’ITG, PPR et PRD ; capacité ITG et PPR (contradiction) ; Capacity ID PRD ; propriétaires (groupes Entra) ; DAG de chaque data product ; classification et criticité ; identité de déploiement Terraform ; schéma officiel du manifeste.

## 5. Contradictions

| N° | Contradiction | Impact | Action |
|---|---|---|---|
| C1 | Capacité ITG/PPR : la capture indique frfrfcdevdp0001 (DC14404E-…), les anciens `deploy.py` 29CDC503-… ; PRD : 8B3B9E06-… sans correspondance dans la capture | Private Link dans la souscription de la capacité | Global : confirmer la capacité de chaque environnement |
| C2 | Plage DEV annoncée en septembre 172.23.63.0/27 sur fralzvnetdev1053 ; plage réelle 172.23.20.0/24 sur fralzvnetdev1055 | documentation obsolète | retenir l’export |
| C3 | Resource group en francecentral, ressources en westeurope | convention de région | Mick : région de référence |
| C4 | ~~Nom des Private Link~~ **résolu** : l’inventaire des ressources du RG frappdevdp0001 confirme `frfrpldevdp<token>managed0001` pour les 15 workspaces (type Microsoft.Fabric/privateLinkServicesForFabric, location Global) ; l’export ARM `FRFRAPEDEVDP001-1` (workspace c09a9722-…) n’y figure pas | aucun | aucune |
| C5 | 172.23.20.14 apparaît deux fois dans le listing DNS, dont pour Référentiel | enregistrement DNS orphelin probable | vérifier la zone DNS |
| C6 | ~~Performance « Engagement » / « Financière »~~ **résolu le 08/11/2026** : le workspace Performance Financière a simplement été renommé `FR - DP - DEV - FAB - BDP - Performance Engagement - MANAGED` (même ID bd480b25-…) | les ressources Azure (PE, Private Link, MPE) gardent le jeton `PERFORMANCEFINANCIERE`, non renommable | conserver ces noms pour l’import ; jeton des nouvelles ressources à fixer avec Mick |
| C7 | **Nos livrables précédents inversaient P2 et P3** (MDS → Framework noté P3) ; la cartographie définit P2 = data product → Framework | manifeste MDS antérieur faux | corrigé dans ce lot |
| C8 | Matrice de la cartographie : colonnes décalées (ligne IBS, lignes ITG/PPR, lignes dev) | lecture des patterns | reconfirmer avec Aimad |
| C9 | Lectures BDP/UCS → ADP/BDP par MPE (75 MPE en DEV) non couvertes par P1–P6 | pattern manquant | P7 PROPOSÉ |
| C10 | Collaborateur → GDS déclaré dans les interconnexions, aucun MPE | flux non configuré | à confirmer |
| C11 | OPENDATA : **non privatisé** (données open source, décision du 08/11/2026), malgré un PE et un Private Link nommés dans le listing ; workspaces PBI SelfX au listing PE sans PE dans le VNet ; GDS (dépôt its-dp-fab-adp-gds-managed) avec PE mais sans DNS | périmètre | OPENDATA tranché ; PBI et DNS GDS à confirmer |
| C16 | Sirene, Compte Engagé, Opportunité, Contact, Lead, Campaign : workspaces DEV confirmés le 08/11/2026 mais absents des exports VNet, DNS et MPE | privatisation DEV à créer (pas à importer) | relever les ID et la capacité avec `inventory-dev-fabric.py --env DEV` |
| C17 | Compte Engagé « à voir s’il remplace le BDP Compte » | deux manifestes possibles pour un même périmètre | à arbitrer |
| C12 | Key Vault sans tags (VNet et RG tagués) | conformité | Mick : tags standard |
| C13 | ~~Hub : même tenant ou Global ?~~ **précisé** : la souscription 1fe4e122-… s’appelle **fr-connectivity** ; elle porte le VNet hub et la zone DNS privée, gérée par Terraform | responsabilité du peering et de la zone | confirmer l’équipe propriétaire de fr-connectivity |
| C18 | Subnet : `purpose` = PrivateEndpoints dans l’export JSON, « Subnet purpose : Default » dans le portail | aucun (valeur calculée par Azure quand le subnet contient des PE) | aucune |
| C19 | Zone DNS : 86 recordsets ; listing DNS fourni : 79 enregistrements dans le périmètre | enregistrements hors périmètre, orphelins (voir C5) ou ceux de GDS, absents du listing : rechercher `69943001-74e6-49d2-a9be-b57abc8f4be9` dans la zone | lister la zone en lecture seule (`az network private-dns record-set list`) |
| C20 | Gateways : DP-FABRIC-GW-PROD et Gateway_prod (contact BI) toutes deux actives avec des utilisateurs PROD | choix de la gateway PRD pour la règle P1 | confirmer avec les administrateurs des gateways |
| C14 | DAG DMND0003667 : architecture par Data Domain (Bronze/Silver/Gold/Flux, F2, une souscription par capacité) ≠ architecture actuelle par data product | cible de la refonte | arbitrage Alexandre / Mick |
| C15 | « Managed » (UCS) / « MANAGED » (autres) | nommage | conserver tel quel (sensibilité à la casse à vérifier) |
