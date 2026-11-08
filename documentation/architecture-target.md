# Architecture cible industrialisée et base descriptive (T4, T11)

Schémas : `diagrams/2-cible-industrialisee.png` et `diagrams/3-chaine-provisioning-deploiement.png`.

## 1. Principe

Trois couches, trois responsables, aucune duplication :

| Couche | Contenu | Source de vérité | Responsable | Outil |
|---|---|---|---|---|
| **Global** | souscriptions, VNet hub, peering, DNS privé, firewall, SPN, capacités | référentiel Global | Global | hors Terraform Data Platform |
| **Configuration réseau d’environnement** | VNet spoke, subnet Private Endpoints, route table, RG, tags | fichier central par environnement | Mick (valeurs fournies par le Global) | modules de Mick |
| **Manifeste data product** | workspace, profil privé, flux, dépendances, identités par référence | `manifests/<cat>/manifest-<dp>.yml` | équipe produit | modules de Mick (lecture du manifeste) |

Le **déploiement des items Fabric** (`config.yml`, `parameter.yml`, `dependencies.yml`, fabric-cicd) reste une chaîne séparée, qui ne démarre qu’après la privatisation.

## 2. Base descriptive : 12 attributs par composant

| # | Composant | Portée | Ressource / paramètre | Fournisseur Terraform (indicatif) | Créé par | Valeur DEV | Source | Dépend de | Approbation | Statut ITG/PPR/PRD | Responsable |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Souscription | Global | — | — | Global | FR-AZR-DP-DEV | capture | — | — | 🔴 manquant | Global |
| 2 | Resource group | partagé env. | `azurerm_resource_group` | azurerm | Global / Mick | frappdevdp0001 | export | 1 | — | 🔴 manquant | Mick |
| 3 | VNet spoke | partagé env. | `azurerm_virtual_network` | azurerm | Global | fralzvnetdev1055 | export | 2 | Global | 🔴 manquant | Global |
| 4 | Subnet Private Endpoints | partagé env. | `azurerm_subnet` | azurerm | Global / Mick | snet-kpmg-backend | export | 3 | Global | 🔴 manquant | Mick |
| 5 | Route table | partagé env. | `azurerm_route_table` | azurerm | Global | fr_rt_fralzvnetdev1055 | export | 3 | Global | 🔴 manquant | Global |
| 6 | Peering hub | Global | `azurerm_virtual_network_peering` | azurerm | Global | fralzvnetdev1055yyfralzvnet0001 | export | 3 | Global | 🔴 manquant | Global |
| 7 | Zone DNS privée | Global | `azurerm_private_dns_zone` | azurerm | Global | non exportée (DNS 10.113.192.100) | export VNet | 6 | Global | 🟠 | Global |
| 8 | Capacité Fabric | partagé env. | `fabric_capacity` (données) | fabric | Global | frfrfcdevdp0001 | capture | 1 | Global | 🔴 C1 | Global |
| 9 | Workspace | par workspace | `fabric_workspace` | fabric | équipe produit / Mick | 18 workspaces de manifeste (12 privatisés en DEV) | DNS, doc 1 | 8 | — | 🟠 ID à vérifier | équipe produit |
| 10 | Private Link service Fabric | par workspace | `Microsoft.Fabric/privateLinkServicesForFabric@2024-06-01` | azapi | module Mick | frfrpldevdp…managed0001 | listing | 9 | — | 🔴 | Mick |
| 11 | Private Endpoint | par workspace | `azurerm_private_endpoint` (sous-ressource `workspace`) | azurerm | module Mick | FRFRAPEFWDEVDP…-1 | VNet | 4, 10 | auto (même tenant) | 🔴 | Mick |
| 12 | Enregistrements DNS | par workspace | `private_dns_zone_group` | azurerm | module Mick / Global | 5 à 6 par workspace | DNS | 7, 11 | Global | 🔴 | Global |
| 13 | Politique de communication (entrant fermé, OAP) | paramètre Fabric | `fabric_workspace_network_communication_policy` | fabric | module Mick | appliquée | cartographie | 11 | sécurité | 🔴 | Mick |
| 14 | Data Connection Rules (P2, P3, P5) | paramètre Fabric | `fabric_workspace_outbound_cloud_connection_rules` | fabric | module Mick | DEV | cartographie | 13 | admin workspace | 🔴 | Mick |
| 15 | Gateway Connection Policy (P1) | par connexion | `fabric_workspace_outbound_gateway_rules` | fabric | module Mick | Framework | cartographie | 13, gateway | admin gateway | 🔴 | Mick |
| 16 | Git outbound (P6) | paramètre Fabric | `fabric_workspace_git_outbound_policy` | fabric | module Mick | DEV uniquement | cartographie | 13 | — | n/a | Mick |
| 17 | Managed Private Endpoint (P4, P7) | par couple | `fabric_workspace_managed_private_endpoint` | fabric | module Mick | 75 lignes | listing MPE | 9 (source et cible) | **propriétaire cible** | 🔴 | Mick + équipe produit |
| 18 | Key Vault et secrets | partagé plateforme | référence uniquement | — | Data Platform | frfrkvdevdp0001 | export | — | sécurité | 🟢 coffre unique | Data Platform |
| 19 | SPN par environnement | Global | référence uniquement | — | Global | 4 SPN | listing | — | Global | 🟢 | Global |

Les noms de ressources Terraform sont indicatifs (provider microsoft/fabric ≥ 1.11) : le choix final appartient aux modules de Mick.

## 3. Ordre de déploiement (T11)

**Provisioning réseau (Terraform)** et **déploiement des items (fabric-cicd)** sont deux chaînes distinctes.

1. Global : souscription, capacité, VNet, subnet, peering, DNS (préalable, hors chaîne).
2. Terraform — configuration d’environnement (si pilotée par Mick).
3. Terraform — **Framework** : workspace, Private Link, Private Endpoint, politique, règles P1/P3/P5, MPE P4.
4. Terraform — **ADP et BDP** (sans ordre entre eux) : workspace, Private Link, Private Endpoint, politique, règles P2, MPE P7.
5. Approbation des MPE par les propriétaires des cibles (étape manuelle, suivie dans l’onglet « Approbations Global »).
6. Terraform — **UCS** (aucune dépendance de déploiement).
7. CD des items : Framework d’abord (porte Framework), puis ADP/BDP, UCS libre.

Un MPE vers une cible pas encore créée est reporté à l’exécution suivante (idempotence), sans bloquer le data product source.
