# Rapport de validation des manifestes

> Schéma **proposé** par l’équipe produit (`dp-fabric-manifest/0.2-proposition`) — ce n’est pas le schéma officiel de Mick.

Légende : 🔴 bloquant · 🟠 à confirmer · ⚪ hors périmètre produit · 🟢 aucun manque

| Data product | Déployable | Bloquants | À confirmer | Hors périmètre | Contrôles de référence | Sécurité |
|---|---|---|---|---|---|---|
| `adp-gds` | 🔴 **non** | 🔴 11 | 🟠 18 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `adp-ibs` | 🔴 **non** | 🔴 11 | 🟠 16 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `adp-mds` | 🔴 **non** | 🔴 11 | 🟠 13 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `adp-referentiel` | 🔴 **non** | 🔴 11 | 🟠 19 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `adp-sirene` | 🔴 **non** | 🔴 17 | 🟠 17 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-campaign` | 🔴 **non** | 🔴 17 | 🟠 20 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-centre-profit` | 🔴 **non** | 🔴 11 | 🟠 19 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-collaborateur` | 🔴 **non** | 🔴 11 | 🟠 32 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-compte-engage` | 🔴 **non** | 🔴 17 | 🟠 36 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-compte` | 🔴 **non** | 🔴 11 | 🟠 23 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-contact` | 🔴 **non** | 🔴 17 | 🟠 30 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-engagement` | 🔴 **non** | 🔴 11 | 🟠 31 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-facture-client` | 🔴 **non** | 🔴 11 | 🟠 43 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-lead` | 🔴 **non** | 🔴 17 | 🟠 20 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-opportunite` | 🔴 **non** | 🔴 17 | 🟠 30 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `bdp-performance-engagement` | 🔴 **non** | 🔴 11 | 🟠 43 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `framework-items` | 🔴 **non** | 🔴 11 | 🟠 94 | ⚪ 2 | 0 remarque(s) | 🟢 OK |
| `ucs-reporting-fees-wip` | 🔴 **non** | 🔴 11 | 🟠 50 | ⚪ 2 | 0 remarque(s) | 🟢 OK |

## Approbations entrantes calculées

Chaque ligne est une approbation ou une règle à prévoir côté **cible** ; elle n’est déclarée qu’une fois (manifeste de la source).

- **adp-gds** : bdp-campaign (P7), bdp-collaborateur (P7), bdp-compte-engage (P7), bdp-contact (P7), bdp-lead (P7), bdp-opportunite (P7), framework-items (P4)
- **adp-ibs** : bdp-facture-client (P7), bdp-performance-engagement (P7), framework-items (P3), framework-items (P4), ucs-reporting-fees-wip (P7)
- **adp-mds** : bdp-centre-profit (P7), bdp-collaborateur (P7), bdp-compte (P7), bdp-compte-engage (P7), bdp-contact (P7), bdp-engagement (P7), bdp-facture-client (P7), bdp-opportunite (P7), bdp-performance-engagement (P7), framework-items (P3), framework-items (P4), ucs-reporting-fees-wip (P7)
- **adp-referentiel** : bdp-collaborateur (P7), bdp-compte (P7), bdp-engagement (P7), bdp-facture-client (P7), bdp-performance-engagement (P7), framework-items (P3), framework-items (P4), ucs-reporting-fees-wip (P7)
- **adp-sirene** : bdp-compte-engage (P7), framework-items (P4)
- **bdp-campaign** : framework-items (P4)
- **bdp-centre-profit** : bdp-collaborateur (P7), bdp-engagement (P7), bdp-facture-client (P7), bdp-performance-engagement (P7), framework-items (P4), ucs-reporting-fees-wip (P7)
- **bdp-collaborateur** : bdp-compte-engage (P7), bdp-contact (P7), bdp-engagement (P7), bdp-facture-client (P7), bdp-opportunite (P7), bdp-performance-engagement (P7), framework-items (P4), ucs-reporting-fees-wip (P7)
- **bdp-compte-engage** : framework-items (P4)
- **bdp-compte** : bdp-facture-client (P7), bdp-performance-engagement (P7), framework-items (P4), ucs-reporting-fees-wip (P7)
- **bdp-contact** : framework-items (P4)
- **bdp-engagement** : bdp-facture-client (P7), bdp-performance-engagement (P7), framework-items (P4), ucs-reporting-fees-wip (P7)
- **bdp-facture-client** : framework-items (P4), ucs-reporting-fees-wip (P7)
- **bdp-lead** : framework-items (P4)
- **bdp-opportunite** : framework-items (P4)
- **bdp-performance-engagement** : framework-items (P4), ucs-reporting-fees-wip (P7)
- **framework-items** : adp-gds (P2), adp-ibs (P2), adp-mds (P2), adp-referentiel (P2), adp-sirene (P2), bdp-campaign (P2), bdp-centre-profit (P2), bdp-collaborateur (P2), bdp-compte (P2), bdp-compte-engage (P2), bdp-contact (P2), bdp-engagement (P2), bdp-facture-client (P2), bdp-lead (P2), bdp-opportunite (P2), bdp-performance-engagement (P2)

## Remarques de référence


## Détail des manques bloquants

| Data product | Ligne | Champ | Marqueur | Quoi | Qui |
|---|---|---|---|---|---|
| `adp-gds` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `adp-gds` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `adp-gds` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `adp-gds` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `adp-gds` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `adp-gds` | 43 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-gds` | 44 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-gds` | 54 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-gds` | 55 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-gds` | 65 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-gds` | 66 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `adp-ibs` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `adp-ibs` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `adp-ibs` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `adp-ibs` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `adp-ibs` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `adp-ibs` | 43 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-ibs` | 44 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-ibs` | 54 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-ibs` | 55 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-ibs` | 65 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-ibs` | 66 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `adp-mds` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `adp-mds` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `adp-mds` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `adp-mds` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `adp-mds` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `adp-mds` | 43 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-mds` | 44 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-mds` | 54 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-mds` | 55 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-mds` | 65 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-mds` | 66 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `adp-referentiel` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `adp-referentiel` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `adp-referentiel` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `adp-referentiel` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `adp-referentiel` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `adp-referentiel` | 43 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-referentiel` | 44 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-referentiel` | 54 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-referentiel` | 55 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-referentiel` | 65 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-referentiel` | 66 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `adp-sirene` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `adp-sirene` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `adp-sirene` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `adp-sirene` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `adp-sirene` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `adp-sirene` | 30 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `adp-sirene` | 31 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `adp-sirene` | 32 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `adp-sirene` | 41 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `adp-sirene` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-sirene` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-sirene` | 52 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `adp-sirene` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-sirene` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `adp-sirene` | 63 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `adp-sirene` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `adp-sirene` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-campaign` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-campaign` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-campaign` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-campaign` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-campaign` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-campaign` | 29 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `bdp-campaign` | 30 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `bdp-campaign` | 31 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `bdp-campaign` | 40 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-campaign` | 41 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-campaign` | 42 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-campaign` | 51 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-campaign` | 52 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-campaign` | 53 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-campaign` | 62 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-campaign` | 63 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-campaign` | 64 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-centre-profit` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-centre-profit` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-centre-profit` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-centre-profit` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-centre-profit` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-centre-profit` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-centre-profit` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-centre-profit` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-centre-profit` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-centre-profit` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-centre-profit` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-collaborateur` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-collaborateur` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-collaborateur` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-collaborateur` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-collaborateur` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-collaborateur` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-collaborateur` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-collaborateur` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-collaborateur` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-collaborateur` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-collaborateur` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-compte-engage` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-compte-engage` | 21 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-compte-engage` | 23 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-compte-engage` | 24 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-compte-engage` | 25 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-compte-engage` | 30 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `bdp-compte-engage` | 31 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `bdp-compte-engage` | 32 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `bdp-compte-engage` | 41 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-compte-engage` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte-engage` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-compte-engage` | 52 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-compte-engage` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte-engage` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-compte-engage` | 63 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-compte-engage` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte-engage` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-compte` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-compte` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-compte` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-compte` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-compte` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-compte` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-compte` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-compte` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-compte` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-contact` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-contact` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-contact` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-contact` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-contact` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-contact` | 29 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `bdp-contact` | 30 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `bdp-contact` | 31 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `bdp-contact` | 40 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-contact` | 41 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-contact` | 42 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-contact` | 51 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-contact` | 52 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-contact` | 53 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-contact` | 62 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-contact` | 63 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-contact` | 64 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-engagement` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-engagement` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-engagement` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-engagement` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-engagement` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-engagement` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-engagement` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-engagement` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-engagement` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-engagement` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-engagement` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-facture-client` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-facture-client` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-facture-client` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-facture-client` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-facture-client` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-facture-client` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-facture-client` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-facture-client` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-facture-client` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-facture-client` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-facture-client` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-lead` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-lead` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-lead` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-lead` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-lead` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-lead` | 29 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `bdp-lead` | 30 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `bdp-lead` | 31 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `bdp-lead` | 40 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-lead` | 41 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-lead` | 42 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-lead` | 51 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-lead` | 52 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-lead` | 53 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-lead` | 62 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-lead` | 63 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-lead` | 64 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-opportunite` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-opportunite` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-opportunite` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-opportunite` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-opportunite` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-opportunite` | 29 | `environments.DEV.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace DEV | équipe produit |
| `bdp-opportunite` | 30 | `environments.DEV.status` | 🔴 A_VERIFIER | existence du workspace DEV et absence de privatisation | équipe produit |
| `bdp-opportunite` | 31 | `environments.DEV.capacityRef` | 🔴 A_VERIFIER | capacité du workspace DEV (frfrfcdevdp0001 attendue) | équipe produit |
| `bdp-opportunite` | 40 | `environments.ITG.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-opportunite` | 41 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-opportunite` | 42 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-opportunite` | 51 | `environments.PPR.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-opportunite` | 52 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-opportunite` | 53 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-opportunite` | 62 | `environments.PRD.workspaceId` | 🔴 A_RENSEIGNER | ID du workspace | équipe produit |
| `bdp-opportunite` | 63 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-opportunite` | 64 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `bdp-performance-engagement` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `bdp-performance-engagement` | 23 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `bdp-performance-engagement` | 25 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `bdp-performance-engagement` | 26 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `bdp-performance-engagement` | 27 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `bdp-performance-engagement` | 45 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-performance-engagement` | 46 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-performance-engagement` | 56 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-performance-engagement` | 57 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `bdp-performance-engagement` | 67 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `bdp-performance-engagement` | 68 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `framework-items` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `framework-items` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `framework-items` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `framework-items` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `framework-items` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `framework-items` | 42 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `framework-items` | 43 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `framework-items` | 53 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `framework-items` | 54 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `framework-items` | 64 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `framework-items` | 65 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
| `ucs-reporting-fees-wip` | 12 | `schemaVersion` | 🔴 A_CONFIRMER_MICK | schéma officiel du manifeste | Mick |
| `ucs-reporting-fees-wip` | 20 | `dataProduct.owner` | 🔴 A_RENSEIGNER | groupe Entra propriétaire du data product | responsable du data product / Alexandre |
| `ucs-reporting-fees-wip` | 22 | `dataProduct.dagReference` | 🔴 A_RENSEIGNER | référence du DAG du data product | architecte |
| `ucs-reporting-fees-wip` | 23 | `dataProduct.classification` | 🔴 A_RENSEIGNER | classification des données (public, interne, confidentiel, restreint) | responsable du data product / sécurité |
| `ucs-reporting-fees-wip` | 24 | `dataProduct.criticality` | 🔴 A_RENSEIGNER | criticité (BC0 à BCx) | responsable du data product |
| `ucs-reporting-fees-wip` | 49 | `environments.ITG.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `ucs-reporting-fees-wip` | 50 | `environments.ITG.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `ucs-reporting-fees-wip` | 67 | `environments.PPR.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `ucs-reporting-fees-wip` | 68 | `environments.PPR.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcdevdp0001, F16) | Global / responsable des capacités |
| `ucs-reporting-fees-wip` | 85 | `environments.PRD.status` | 🔴 A_VERIFIER | existence et état du workspace | équipe produit |
| `ucs-reporting-fees-wip` | 86 | `environments.PRD.capacityRef` | 🔴 A_CONFIRMER_GLOBAL | capacité de l’environnement (frfrfcprddp0001, F32) | Global / responsable des capacités |
