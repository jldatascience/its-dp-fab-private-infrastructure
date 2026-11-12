# Questions prioritaires pour Mick (Livrable 6)

## Priorité 1 — bloquant avant ITG

1. **Frontière mutualisé / par workspace** : VNet, subnet, DNS, peering dans la configuration d’environnement ; Private Link, Private Endpoint, règles Fabric dans le manifeste. D’accord ?
2. **Schéma officiel** du point d’entrée Data Platform : format, nom des champs, version, date de publication ?
3. **Configuration réseau ITG, PPR, PRD** : qui obtient du Global la souscription, le VNet, le subnet et la plage IP (≈ 108 IP pour 18 workspaces, hors croissance) ?
4. ~~**Capacités**~~ **résolu le 12/11/2026** : DEV, ITG et PPR sur frfrfcdevdp0001 (DC14404E-…), PRD sur gomfcaprodeuwfabricdataplatformfr0001 (8B3B9E06-…). Reste à connaître la souscription de la capacité PRD (Private Link).
5. **Identité de déploiement Terraform** : SPN existants ou identité dédiée ? Fédération OIDC / WIF disponible ?
6. **Reprise de DEV** : import des 16 PE et des MPE, ou DEV laissé hors Terraform ?

7 bis. **Zone DNS privée** : elle est gérée par Terraform dans fr-connectivity. Qui écrit les enregistrements A des nouveaux Private Endpoints (DNS zone group de ses modules ou code connectivité) sans créer de dérive ? Une seule zone pour les 4 environnements ? Son unique lien VNet vise-t-il le hub ?
7 ter. **Gateways** : quelle gateway pour ITG et PPR (DP-FABRIC-GW-HORS-PROD ?) et pour PRD (DP-FABRIC-GW-PROD ou Gateway_prod) ? Les connexions `<OBJET>_<ENV>_DP_FABRIC` hors DEV existent-elles ?

## Priorité 2 — conception

7. Accepte-t-il la déclaration des flux côté **porteur de la règle**, avec calcul des approbations côté cible ?
8. **P7** (lecture inter-data products par MPE) : nouveau pattern ou rattachement à P4 ?
9. Nommage hors DEV : nomenclature DEV transposée (FRFRAPEFW<ENV>DP<TOKEN>MANAGED0001-1, frfrpl<env>dp<token>managed0001), décidée le 08/11/2026 — ses modules peuvent-ils la générer à partir du jeton ?
10. Comment les modules gèrent-ils l’**approbation manuelle** des MPE (attente, reprise) ?
11. Un manifeste unique pour 4 environnements, ou un fichier par environnement ?
12. Région de référence : westeurope (ressources) ou francecentral (RG) ?

## Priorité 3 — périmètre

13. Workspaces Power BI du UCS : privatisés ou non ? OPENDATA n’est pas privatisé (données open source) : si un workspace privatisé (Framework, BDP) doit y lire ou y écrire, quelle règle sortante l’autorise malgré l’Outbound Access Protection ?
13 bis. Sirene, Opportunité, Contact, Lead, Campaign : privatisation DEV créée par Terraform dès la première exécution, ou manuellement comme pour les autres ? Jeton de nommage de leurs ressources ?
14. Référentiel : les workspaces ITG, PPR, PRD existent (préfixes d’ID connus) ; confirmer qu’ils sont privatisés tels quels (import) et l’ordre vis-à-vis du premier déploiement des items (dépôt encore vide).
15. Tags standard (le Key Vault n’en a aucun) ?
16. Les 12 contrôles normalisés : lesquels s’appliquent aux manifestes ?
17. Architecture du DAG DMND0003667 (par Data Domain) : cible de la refonte ou cas particulier ?
