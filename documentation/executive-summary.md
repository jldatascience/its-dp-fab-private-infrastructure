# Synthèse exécutive (Livrable 7)

**Constat** : DEV est entièrement privatisé à la main. Il compte :
- 15 workspaces ;
- 16 Private Endpoints (dont le Key Vault) et 85 adresses IP ;
- 75 lignes de MPE, dont 10 « À créer » vers Référentiel.

Six data products ajoutés le 08/11/2026 (ADP Sirene ; BDP Compte Engagé, Opportunité, Contact, Lead, Campaign) ont leurs dépôts et workspaces, mais ne sont pas privatisés en DEV. ADP GDS a désormais son dépôt et un manifeste. ADP OPENDATA n’est **pas privatisé** (données open source) : il n’a pas de manifeste.

ITG, PPR et PRD n'ont aucune donnée réseau. Les 18 manifestes sont complets sur le plan structurel. Aucun n'est déployable. Les ID des workspaces ITG, PPR et PRD des anciens `deploy.py` sont confirmés (08/11/2026). Les 12 manifestes dont les ID sont connus dans les 4 environnements (MDS, Référentiel, IBS, 6 BDP, Framework, UCS, GDS) gardent chacun 11 marqueurs bloquants :
- 1 sur le schéma ;
- 4 sur la gouvernance (propriétaire, DAG, classification, criticité) ;
- 6 sur ITG, PPR et PRD (état de privatisation, capacité) ;

Les noms des ressources réseau en ITG, PPR et PRD ne bloquent plus : Private Endpoint, Private Link, MPE, resource group, VNet, subnet et route table reprennent la nomenclature DEV (décision du 08/11/2026). Les 6 nouveaux data products en ont 17 : leurs 3 ID hors DEV et 3 points pour DEV (ID, état, capacité).

| # | Question | Réponse |
|---|---|---|
| 1 | Fichiers à créer | 18 manifestes, 1 modèle, 10 fichiers d'inventaire, 3 scripts (inventaires en lecture seule, validateur), 13 documents, un rapport de validation, 3 schémas, 1 classeur de suivi |
| 2 | Fichiers communs | `service-principals.yml`, `keyvault-references.yml`, `environment-network-reference.yml`, `manifest-template.yml`, scripts |
| 3 | Fichiers par data product | un `manifest-<dp>.yml` (les 4 environnements dans le même fichier) |
| 4 | Un manifeste par environnement ? | Non. On utilise un seul fichier, et seuls les ID et la capacité changent. Ce choix est à confirmer par Mick (question 11). |
| 5 | Hooks ? | Aucun. Le bloc `extensions: {}` est vide ; P7 fait l'objet d'une demande d'évolution. |
| 6 | Fichiers de Mick | schéma officiel, modules Terraform, configuration réseau par environnement, standard d'identité |
| 7 | Informations à tirer de DEV | ID des workspaces, noms des PE et des PLS, nombre d'IP, MPE, DNS, région et tags. Elles sont déjà extraites ; il reste à les confirmer avec `inventory-dev-azure.sh`. |
| 8 | Manquant pour ITG, PPR et PRD | souscription, RG, VNet et subnet, plage IP, peering, capacité (C1), noms Azure hors DEV, ID des workspaces à vérifier |
| 9 | Références Key Vault | coffre unique `frfrkvdevdp0001`, 12 secrets `<ENV>-AZURE-*`. Les secrets ITG, PPR et PRD expirent le **17/01/2027**. Cible : fédération d'identité. |
| 10 | Nommage | Workspaces confirmés pour les 4 environnements. Private Endpoint, Private Link et MPE : nomenclature DEV transposée (`FRFRAPEFW<ENV>DP<TOKEN>MANAGED0001-1`, `frfrpl<env>dp<token>managed0001`). Resource group, VNet, subnet et route table : nomenclature DEV transposée ; souscription, plage IP, DNS et peering : Global. |
| 11 | Éviter les doublons Terraform | Chaque flux est déclaré une seule fois, côté porteur de la règle. Le réseau reste mutualisé hors manifeste. L'existant est repris par `import` déclaratif, avec un plan sans destruction. |
| 12 | Étapes bloquantes avant ITG | schéma officiel, configuration réseau ITG, capacité ITG, identité Terraform, propriétaires et DAG, décision sur la reprise de DEV |
| 13 | Validations du Global | réseau ITG/PPR/PRD, capacités, écriture des enregistrements dans la zone DNS gérée par Terraform (fr-connectivity), peering, gateways ITG/PPR/PRD, renouvellement des secrets |
| 14 | Fichiers utilisables tout de suite | scripts d'inventaire, validateur, inventaires DEV, références KV et SPN, documentation, classeur |
| 15 | Fichiers provisoires | les 18 manifestes et le modèle (schéma proposé, `deployable: false`), plus `environment-network-reference.yml` |

**ADP Référentiel** : manifeste `manifest-adp-referentiel.yml` aligné sur le dépôt `its-dp-fab-adp-referentiel-managed` (workspaces des 4 environnements confirmés le 03/11/2026, préfixes des ID ITG/PPR/PRD connus, dépôt sans item, Git Integration DEV à connecter, 3 service connections ARM à créer).

**Correction apportée par ce lot** : les livrables précédents inversaient P2 et P3. Le flux MDS → Framework est un **P2**.

**À faire en premier** :
1. Valider avec Mick la frontière entre ressources mutualisées et ressources par workspace.
2. Lancer l'inventaire en lecture seule pour confirmer les ID ITG, PPR et PRD.
