# Proposition de schéma de manifeste (T5, T6, T7)

> **Proposition de l’équipe produit.** Ce n’est pas le schéma officiel de Mick. Les noms de champs seront alignés sur son schéma dès sa publication ; le contenu (les valeurs et leurs sources) reste réutilisable.

## 1. Stratégie retenue

| Choix | Décision proposée | Raison |
|---|---|---|
| Schéma | central, possédé par Mick | un seul format pour tous les points d’entrée |
| Manifeste | **un par data product**, 4 environnements dans le même fichier | les flux et dépendances sont les mêmes partout ; seuls les ID et la capacité changent |
| Réseau | **configuration par environnement**, possédée par l’équipe centrale | VNet, subnet, DNS, peering sont mutualisés : ils ne figurent dans aucun manifeste |
| Extensions | bloc `extensions: {}` vide par défaut | toute exception passe par une demande d’évolution |
| Hooks | **aucun hook séparé** | P1 à P7 couvrent les besoins actuels |
| Flux | déclarés une seule fois, côté workspace qui **porte la règle** | évite la double déclaration ; le validateur calcule les approbations côté cible |
| Secrets | références Key Vault uniquement | aucune valeur dans Git |

## 2. Structure

| Bloc | Contenu | Remarque |
|---|---|---|
| `schemaVersion` | `dp-fabric-manifest/0.2-proposition` | marqué `[A_CONFIRMER_MICK]` bloquant |
| `deployable` | toujours `false` à l’écriture | recalculé par le validateur |
| `dataProduct` | id, name, category, repository, owner, responsibleTeam, dagReference, classification, criticality | |
| `environments.<ENV>` | workspaceName, workspaceId, status, capacityRef, gitIntegration, existingResources | `existingResources` sert à l’import Terraform |
| `privatisation` | networkProfile, inbound, outbound, dns, sharedNetworkRef | aucune IP, aucun nom de VNet |
| `flows[]` | id, pattern, direction, source, target, mechanism, ruleCarriedBy, protocol, port, businessJustification, dagReference, approvalOwner, validationStatus par environnement, evidence | |
| `dependencies` | deployment.framework, frameworkItemsConsumed, data[], externalConnections[] | données ≠ déploiement |
| `security` | identityRef, federatedIdentity, keyVaultRefs, entraGroups | |
| `extensions` | `{}` | |
| `dependencies.itemDeployment` | références vers `config.yml`, `dependencies.yml`, `parameter.yml` du dépôt (Référentiel) | lien documentaire, jamais piloté par Terraform |
| `traceability` | sources, validatedOn, validatedBy, completeness, globalTickets | |

## 3. Marqueurs (T7)

Format d’un champ manquant :

```yaml
owner: null   # [A_RENSEIGNER] Quoi : … | Pourquoi : … | Qui : … | Où : … | Bloquant : oui
```

| Marqueur | Usage | Couleur |
|---|---|---|
| `[A_RENSEIGNER]` | donnée que l’équipe produit doit fournir | rouge si bloquant, sinon orange |
| `[A_VERIFIER]` | valeur présente mais non fiable | orange (rouge si bloquant) |
| `[A_CONFIRMER_MICK]` | choix de schéma ou de standard | orange (rouge si bloquant) |
| `[A_CONFIRMER_GLOBAL]` | valeur détenue par le Global | rouge si bloquant |
| `[HORS_PERIMETRE_PRODUIT]` | fournie par la configuration centrale | gris |

La couleur est produite par le rapport HTML, le Markdown et le classeur Excel ; la syntaxe YAML n’est jamais modifiée pour obtenir une couleur. **Un seul marqueur bloquant rend le manifeste non déployable.**

## 4. Data products couverts

| Manifeste actif | Suivi seulement (`inventory/data-products-tracking.csv`) |
|---|---|
| ADP MDS, Référentiel, IBS, Sirene, GDS | OPENDATA (non privatisé : données open source) |
| BDP Collaborateur, Compte, Centre de Profit, Engagement, Facture Client, Performance Engagement, Opportunité, Contact, Lead, Campaign | |
| Framework Items | |
| UCS Reporting Fees & WIP | |
