# fabric-private-infrastructure

Préparation de l’industrialisation Terraform de la privatisation Microsoft Fabric — French Data Platform KPMG.

> **Statut : PROVISOIRE.** Les manifestes suivent un schéma **proposé** par l’équipe produit (`dp-fabric-manifest/0.2-proposition`) ; ce n’est **pas** le schéma officiel de Mick. Aucun manifeste n’est déployable. Aucune ressource réelle n’a été modifiée.

## ADP Référentiel

Le dépôt `its-dp-fab-adp-referentiel-managed` (README, CHANGELOG et `CICD/` du 03/11/2026) apporte :
- les noms des workspaces `FR - DP - <ENV> - FAB - ADP - Referentiel - MANAGED` pour DEV, ITG, PPR et PRD (confirmés le 03/11/2026, tiret simple) ;
- les ID des workspaces ITG (`13b7d0a0-4ff3-4dca-a3d2-e15974b614e7`), PPR (`161b78a6-bded-43c1-97fd-96e7aec40a2e`) et PRD (`ba74b427-a836-4686-a195-252f747d867e`), communiqués le 08/11/2026 (leurs préfixes figurent dans `guid_policy.forbidden_prefixes`) ;
- l’état du dépôt : aucun item Fabric (`fabric/.gitkeep`), `inventory_status: pending`, Git Integration DEV non connectée ;
- le Framework comme unique prérequis de déploiement, `framework.items`, `connections`, `variable_libraries` et `data_dependencies` vides, à relever ;
- le coffre unique `frfrkvdevdp0001` et 3 service connections ARM ITG, PPR, PRD à créer en fédération d’identité ;
- l’outillage de référencement dynamique `CICD/ref_dynamique/01` à `04`, en lecture seule, réutilisable pour relever les ID (`02_fab_cli.py --env <ENV>`).

## Data products ajoutés le 08/11/2026

Dépôts et workspaces des 4 environnements confirmés pour ADP Sirene et BDP Opportunité, Contact, Lead et Campaign
(`FR - DP - <ENV> - FAB - ADP - Sirene - MANAGED`, `FR - DP - <ENV> - FAB - BDP - Opportunite - MANAGED`, etc.).
BDP Compte Engagé, également communiqué le 08/11/2026, est supprimé le 12/11/2026 (voir plus bas).
Aucun de ces 5 data products n’est privatisé en DEV : leurs manifestes portent 8 marqueurs bloquants (1 de plus pour DEV).

ADP GDS : dépôt `its-dp-fab-adp-gds-managed` (indiqué le 08/11/2026) ; manifeste actif. Noms et ID des workspaces des 4 environnements
communiqués le 08/11/2026 (DEV 69943001-…, ITG 071742c7-…, PPR 87241b71-…, PRD 55038f5c-…). Workspace DEV privatisé (PE, 5 IP)
mais sans enregistrement DNS listé (15 marqueurs bloquants).

ADP OPENDATA : **non privatisé** (données open source, décision du 08/11/2026). Aucun manifeste ; suivi seulement dans
`inventory/data-products-tracking.csv` (dépôt `its-dp-fab-adp-opendata-managed`).

## Mise à jour du 12/11/2026

Sources : liste des workspaces par environnement (« Suivi des workspaces », 80 workspaces), dépôts de la chaîne CI/CD
initialisés sur le socle `its-dp-fab-cicd-common` v1.5.0, cartographie simplifiée des flux Microsoft Fabric.

- ID des workspaces : les 4 environnements d'ADP Sirene et des BDP Campaign, Contact, Lead et Opportunité sont renseignés ;
  tous les manifestes concordent avec la liste (nom, ID, capacité).
- Capacités : `capacityRef` renseigné pour chaque environnement, `frfrfcdevdp0001` (DC14404E-…) pour DEV, ITG et PPR,
  `gomfcaprodeuwfabricdataplatformfr0001` (8B3B9E06-…) pour PRD. La contradiction C1 est close.
- Propriétaire : `owner` = `FR-SG AAD ITS DAS Fabric Admin`, groupe Entra qui approuve les MPE entrants (colonne de la liste,
  identique pour les 80 workspaces).
- Nouveaux manifestes : `manifest-ucs-hubspot.yml`, `manifest-ucs-referentiel.yml`, `manifest-ucs-mybsc-snow.yml` (workspaces
  `FR - DP - <ENV> - FAB - UCS - <Nom> - Managed`, non privatisés en DEV). UCS Referentiel porte un flux P2 vers le Framework
  (cartographie) ; il est signalé, car la matrice du socle CI/CD (R5) interdit toute dépendance de déploiement à un UCS.
- MyBSC / SNOW : ID PPR `8f97d25d-…` (la liste donnait auparavant l'ID DEV).
- BDP Compte Engagé : supprimé (ni dépôt ni workspace dans la liste ; décision du 12/11/2026, contradiction C17 close).
  Son manifeste, ses 4 lignes d'inventaire et le flux P4 du Framework vers lui sont retirés.
- `inventory/workspaces-by-environment.csv` et `tracking/Suivi_privatisation_Fabric.xlsx` sont alignés ; le rapport de validation
  et `tracking/missing-parameters.csv` sont régénérés.

## Arborescence

```
manifests/
  adp/        manifest-adp-mds.yml, manifest-adp-referentiel.yml, manifest-adp-ibs.yml, manifest-adp-sirene.yml, manifest-adp-gds.yml
  bdp/        10 manifestes BDP (dont Opportunité, Contact, Lead, Campaign, ajoutés le 08/11/2026)
  framework/  manifest-framework.yml
  ucs/        manifest-ucs-reporting-fees-wip.yml, manifest-ucs-hubspot.yml, manifest-ucs-referentiel.yml, manifest-ucs-mybsc-snow.yml
  templates/  manifest-template.yml
inventory/    inventaires DEV (JSON, CSV), références Key Vault et SPN, faits réseau
scripts/      inventory-dev-azure.sh, inventory-dev-fabric.py, validate-manifests.py (lecture seule)
documentation/ architecture, schéma, patterns, nommage, contrat, reprise, cycle de vie, RACI,
               questions, synthèse, rapport de validation, diagrammes
tracking/     Suivi_privatisation_Fabric.xlsx, missing-parameters.csv
```

## Emplacement local

Même chemin sur les deux postes, à côté des dépôts de la chaîne CI/CD :
`~/projects/fabric-private-infrastructure` (iMac) et `C:\projects\fabric-private-infrastructure` (PC KPMG).
Les sorties brutes des inventaires (`_inventaire/`) sont exclues par `.gitignore`. Sous Windows, `inventory-dev-azure.sh`
se lance depuis Git Bash ; les scripts Python fonctionnent tels quels.

## Démarrage

```bash
pip install pyyaml
python3 scripts/validate-manifests.py          # rapport dans documentation/manifest-validation-report.html
./scripts/inventory-dev-azure.sh ./_inventaire  # lecture seule (az login requis)
```

## Règles

- Aucun secret, aucune adresse IP, aucun nom de VNet dans un manifeste.
- Une valeur inconnue reste `null` avec un marqueur `[A_RENSEIGNER]`, `[A_VERIFIER]`, `[A_CONFIRMER_MICK]`, `[A_CONFIRMER_GLOBAL]` ou `[HORS_PERIMETRE_PRODUIT]`.
- Un flux est déclaré dans le manifeste du workspace qui porte la règle.
- Aucun `terraform import`, `apply` ou `destroy` sans plan relu et validé.
- La privatisation (Terraform) est distincte du déploiement des items (`config.yml`, `parameter.yml`, `dependencies.yml`).

Point d’entrée : `documentation/executive-summary.md`.
