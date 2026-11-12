# Architecture DEV réelle (T2)

Reconstitution à partir des exports du 08/11/2026. Schéma : `diagrams/1-reseau-dev-existant.png`.

## 1. Socle Azure

| Élément | Valeur | Portée |
|---|---|---|
| Tenant | deff24bb-2089-4400-8c8e-f71e680378b2 | Global |
| Souscription | FR-AZR-DP-DEV (0c53c37e-2ed2-4d58-b147-8f80763294ce), management group FR-MG-CH-Root-BYOS, EA | Global |
| Resource group | frappdevdp0001 — francecentral — tags env=dev, platform=d&a, service=dataplatform, app=dataplatform | partagé |
| VNet spoke | fralzvnetdev1055 — westeurope — 172.23.20.0/24 — DNS 10.113.192.100 | partagé |
| Subnet | snet-kpmg-backend — 172.23.20.0/24 — purpose PrivateEndpoints — sans NSG, sans NAT, defaultOutboundAccess=false, privateEndpointNetworkPolicies=Disabled | partagé |
| Route table | fr_rt_fralzvnetdev1055 (routes non exportées) | partagé |
| Peering | fralzvnetdev1055yyfralzvnet0001 → fralzvnet0001 (10.113.192.0/22, RG frinfalzconnectivityhub0001) — Connected, allowForwardedTraffic=true, useRemoteGateways=false | Global |
| Key Vault | frfrkvdevdp0001 + PE FRFRAPEKVDEVDP0001 (1 IP) | partagé plateforme |
| Capacité | frfrfcdevdp0001 F16 | partagé |

**Principe constaté** : un VNet et un subnet uniques pour l’environnement ; chaque workspace privatisé possède son Private Link service Fabric (global) et son Private Endpoint dans ce subnet.

### Compléments (captures et exports du 08/11/2026)

- **Subnet** `snet-kpmg-backend` (ID `/subscriptions/0c53c37e-…/resourceGroups/frappdevdp0001/…`) : private subnet (aucun accès sortant par défaut), aucun NAT, aucun NSG, aucun service endpoint, aucune délégation, route table `fr_rt_fralzvnetdev1055`, politique réseau des Private Endpoints Disabled, préfixe non modifiable car utilisé.
- **Zone DNS privée** `privatelink.fabric.microsoft.com` : souscription **fr-connectivity** (1fe4e122-…), RG `frinfalzconnectivityprivatedns0001`, location global, 86 recordsets, **1 lien VNet**, tag `Status: Managed by Terraform`.
- **Private Link services** (inventaire des ressources du RG) : `frfrpldevdp<token>managed0001`, un par workspace, type `Microsoft.Fabric/privateLinkServicesForFabric`, location Global ; NIC des Private Endpoints `<PE>-nic`, NIC du PE Key Vault `FRFRAPEKVDEVDP0001.nic.90d6fd98-f532-4db9-868b-2266f60bcbaa`.
- **Key Vault** : RBAC sans access policy, aucune règle IP ni VNet, accès par le seul Private Endpoint (connexion approuvée), 12 secrets à l’état Enabled.

### Gateways et connexions

| Gateway | Contact | Connexions DEV relevées |
|---|---|---|
| DP-FABRIC-GW-HORS-PROD | fr-svcdp-dev@kpmg.fr | MDS_DEV_DP_FABRIC (SQL Server FRPARAPP9042\SQLDEV, base MDM), STAGING_DEV_DP_FABRIC (même serveur, base STAGING) — authentification Windows |
| DP-FABRIC-GW-PROD | fr-svcdp-prd@kpmg.fr | aucune listée |
| Gateway_prod | fr-svcbi-prod@kpmg.fr | aucune listée (contact BI) |

Connexion cloud : `DP-Fabric-Global-APR` (Pipelines de données Fabric, Service Principal), utilisée par les Invoke Pipeline (P2, P3). Détail : `inventory/gateways-and-connections.yml`.

## 2. Workspaces privatisés en DEV

| Workspace | ID | Private Endpoint | IP | DNS |
|---|---|---|---|---|
| ADP MDS | a699158a-f604-431c-b9f4-aff776a02c5d | FRFRAPEFWDEVDPADPMDSMANAGED0001-1 | 6 | 6 |
| ADP Référentiel | 4c6b33a2-d61c-4c92-8cea-80eadcf277d2 | FRFRAPEFWDEVDPADPREFERENTIELMANAGED0001-1 | 5 | 5 |
| ADP IBS | 4c55fb1e-4c8a-457c-8eea-26fd38cde682 | FRFRAPEFWDEVDPADPIBSMANAGED0001-1 | 6 | 6 |
| ADP GDS (dépôt its-dp-fab-adp-gds-managed) | 69943001-74e6-49d2-a9be-b57abc8f4be9 | FRFRAPEFWDEVDPADPGDSMANAGED0001-1 | 5 | aucun |
| BDP Centre de Profit | 46c8f043-e4a2-4c6f-9591-35ad9c6d6006 | FRFRAPEFWDEVDPBDPCENTREDEPROFITMANAGED0001-1 | 6 | oui |
| BDP Collaborateur | 7679a1ba-345d-46b0-a4d0-4bc05d065f3f | FRFRAPEFWDEVDPBDPCOLLABORATEURMANAGED0001-1 | 6 | oui |
| BDP Compte | f60f7870-63a5-456c-8db2-daa264c67114 | FRFRAPEFWDEVDPBDPCOMPTEMANAGED0001-1 | 6 | oui |
| BDP Engagement | eccf49e0-58e9-4fbf-8256-e446eebca01d | FRFRAPEFWDEVDPBDPENGAGEMENTMANAGED0001-1 | 6 | oui |
| BDP Facture Client | dd280c49-24d1-43bf-b92b-c720be387a0d | FRFRAPEFWDEVDPBDPFACTURECLIENTMANAGED0001-1 | 6 | oui |
| BDP Performance Engagement (ex-Performance Financière, renommé) | bd480b25-4e5f-4758-bcf8-2c229310b4c4 | FRFRAPEFWDEVDPBDPPERFORMANCEFINANCIEREMANAGED0001-1 | 6 | oui |
| Framework | 779f53bb-fc39-4c1a-a580-e9794416486b | FRFRAPEFWDEVDPFRAMEWORKMANAGED0001-1 | 5 | oui |
| UCS Reporting Fees & WIP | 6bb479d1-2e8d-4037-89de-4753ea3da38a | FRFRAPEFWDEVDPUCSREPORTINGFEESETWIPMANAGED0001-1 | 5 | oui |
| DEV Daniels / Houssem / Yassine | 42463408-… / ce00f62a-… / 5a061fb6-… | FRFRAPEFWDEVDP<NOM>MANAGED0001-1 | 5 / 5 / 6 | oui |

DEV Jalel (ajouté le 12/11/2026) : workspace personnel `FR - DP - DEV - FAB - DEV - JALEL - MANAGED`, **en cours de privatisation** (PE prévu `FRFRAPEFWDEVDPJALELMANAGED0001-1`, capacité `frfrfcdevdp0001`) ; absent des exports DEV (aucun PE, DNS ni MPE à ce jour) ; ID à relever avec `02_fab_cli.py --env DEV`.

Noms exacts : `inventory/network-components.csv`, `inventory/dns-records-dev.csv`. Total : 85 IP utilisées sur 251 utilisables (Key Vault compris).

## 3. Managed Private Endpoints (75 lignes)

- suffixe `-1` = Private Endpoint entrant ; `-2` Houssem, `-3` Daniels, `-4` Yassine ; MPE inter-workspaces à partir de `-5` ;
- Framework → 9 ADP/BDP (P4) ;
- BDP et UCS → ADP/BDP (lecture, P7 proposé) conformes à la liste des interconnexions ;
- MDS → workspaces personnels (noms irréguliers `…0001-01`) ;
- 10 MPE vers Référentiel (Framework, BDP, UCS, workspaces personnels) au statut « À créer ».

Détail : `inventory/managed-private-endpoints-dev.csv`.

## 4. Identités et secrets

4 SPN (un par environnement), secrets client stockés dans l’unique Key Vault frfrkvdevdp0001 (12 secrets nommés `<ENV>-AZURE-CLIENT-ID|SECRET|TENANT-ID`). Les secrets ITG, PPR et PRD expirent le **17/01/2027**. Voir `inventory/keyvault-references.yml`.

## 5. Points d’attention

- Aucun NSG sur le subnet : la sécurité repose sur les politiques Fabric et le firewall du hub (à confirmer par le Global).
- Workspaces Power BI du UCS : non privatisés en DEV.
- ADP OPENDATA : **hors privatisation** (données open source, décision du 08/11/2026) ; le listing nommait un PE et un Private Link qui n’ont jamais été créés.
- Workspaces ajoutés le 08/11/2026, **non privatisés en DEV** (aucun PE, DNS ni MPE) : ADP Sirene ; BDP Opportunite, Contact, Lead, Campaign. Leur privatisation DEV demandera environ 25 à 30 IP de plus (5 à 6 par workspace) dans le subnet, qui en a 166 de libres.
- L’état réseau de ITG, PPR et PRD n’est pas connu : aucun export.
