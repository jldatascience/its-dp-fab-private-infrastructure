# Cycle de vie cible d’un data product (T14)

| # | Étape | Automatisable | Acteur | Reprise / idempotence |
|---|---|---|---|---|
| 1 | Demande et DAG du data product | non | architecte | — |
| 2 | Création du dépôt Azure DevOps à partir du socle commun | oui | Ops | rejouable (existe → ignoré) |
| 3 | Copie du modèle de manifeste et saisie | non | équipe produit | — |
| 4 | Validation du manifeste (`validate-manifests.py`) | oui | CI | rejouable |
| 5 | Revue du manifeste (pull request) | non | Mick, sécurité | — |
| 6 | Vérification des prérequis Global (souscription, capacité, réseau, SPN) | oui (contrôle) | CI | bloque si absent |
| 7 | Création du workspace et affectation à la capacité | oui | Terraform | import si existant |
| 8 | Rôles du workspace (groupes Entra, SPN) | oui | Terraform | déclaratif |
| 9 | Private Link service et Private Endpoint | oui | Terraform | déclaratif |
| 10 | Enregistrements DNS | oui / Global | Terraform ou Global | vérifié par `nslookup` |
| 11 | Politique de communication (entrant fermé, OAP) | oui | Terraform | déclaratif |
| 12 | Règles sortantes (P1, P2, P3, P5, P6) | oui | Terraform | déclaratif |
| 13 | MPE (P4, P7) | oui | Terraform | cible absente → reporté |
| 14 | **Approbation des MPE** par les propriétaires des cibles | **non (manuel)** | propriétaires | suivi dans le classeur |
| 15 | Déploiement des items (fabric-cicd, porte Framework) | oui | CD du socle | rejouable |
| 16 | Contrôles post-déploiement et mise à jour de la traçabilité | oui | CI | rejouable |

Étapes relevant du Global : 6 (fourniture), 10 (zone DNS), réseau du hub, SPN. En cas d’échec, la chaîne reprend à l’étape en erreur : toutes les étapes automatisées sont déclaratives.

**Décommissionnement** (hors périmètre de ce lot) : suppression des MPE entrants côté sources, puis Private Endpoint, puis Private Link, puis workspace — uniquement après validation.
