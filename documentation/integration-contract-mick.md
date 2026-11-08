# Contrat d’intégration avec Mick (T12)

## 1. Ce que l’équipe produit fournit

| Livrable | Format | Emplacement |
|---|---|---|
| Un manifeste par data product | YAML, schéma proposé puis officiel | `manifests/<cat>/` |
| Inventaire DEV assaini | JSON / CSV | `inventory/` |
| Références Key Vault et SPN | YAML (noms uniquement) | `inventory/keyvault-references.yml`, `inventory/service-principals.yml` |
| Faits réseau DEV et manques ITG/PPR/PRD | YAML informatif | `inventory/environment-network-reference.yml` |
| Rapport de complétude | MD / HTML / CSV | `documentation/manifest-validation-report.*`, `tracking/` |

## 2. Ce que Mick fournit

| Élément | Attendu |
|---|---|
| Schéma officiel du manifeste | nom, version, champs obligatoires, validation |
| Modules Terraform | Private Link, Private Endpoint, politiques Fabric, règles, MPE (avec Iskander et Mohamed) |
| Configuration réseau par environnement | VNet, subnet, RG, tags, région |
| Standard d’identité | identité de déploiement Terraform, fédération OIDC / WIF |
| Contrôles normalisés | les 12 contrôles, leur application hors DEV |
| Mode de reprise de l’existant | `import` déclaratif, garde-fou anti-destruction |

## 3. Frontière à valider en priorité

| Mutualisé (configuration d’environnement) | Par workspace (manifeste) |
|---|---|
| VNet, subnet, route table, peering, zone DNS | Private Link service, Private Endpoint, enregistrements DNS du workspace |
| Région, tags, resource group | politique entrante / sortante, DCR, Git outbound, MPE |

## 4. Règles du contrat

1. Le manifeste ne contient aucune IP, aucun nom de VNet ni de subnet, aucun secret.
2. Les flux sont déclarés côté porteur de la règle ; Mick calcule les approbations.
3. Un manifeste avec un marqueur bloquant n’est jamais appliqué.
4. Aucun `terraform apply`, `import` ou `destroy` sans plan relu et validé.
5. `extensions` reste vide sauf demande d’évolution acceptée.

## 5. Fiche de demande d’évolution (modèle)

| Champ | Valeur |
|---|---|
| N° | DE-AAAA-NN |
| Demandeur | |
| Data product(s) | |
| Besoin | (ex. pattern P7, workspace Power BI privatisé) |
| Justification métier | |
| Pattern concerné / nouveau | |
| Impact sécurité | |
| Validation sécurité (Aimad) | |
| Décision Mick | acceptée / refusée / reportée |
| Version du schéma | |

### Demandes ouvertes

| N° | Objet |
|---|---|
| DE-01 | Pattern **P7** : lecture inter-data products par MPE |
| DE-02 | Bloc `existingResources` pour l’import de l’existant DEV |
| DE-03 | Workspaces Power BI du UCS : privatisation ou exclusion |
| DE-04 | Champ `dependencies.itemDeployment` : lien documentaire entre le manifeste et la configuration de déploiement du dépôt |
| DE-05 | Flux P5 du Framework vers l’API Fabric (référencement dynamique) |
