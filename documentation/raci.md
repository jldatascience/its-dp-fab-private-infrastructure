# RACI

R = réalise · A = approuve · C = consulté · I = informé

| Activité | Équipe produit (Jérémy) | Mick | Iskander / Mohamed | Alexandre (architecte) | Sécurité (Aimad) | Global | Ops |
|---|---|---|---|---|---|---|---|
| Schéma officiel du manifeste | C | **A/R** | C | C | C | I | I |
| Manifestes des data products | **R** | A | I | C | C | I | I |
| Inventaire DEV (lecture seule) | **R** | I | I | I | I | C | I |
| Configuration réseau par environnement | C | **A/R** | C | C | C | R (valeurs) | I |
| Souscriptions, VNet, peering, DNS, firewall | I | C | I | C | C | **A/R** | I |
| Capacités Fabric | C | C | I | C | I | **A/R** | I |
| SPN et Key Vault | C | C | I | I | A | **R** | R |
| Modules Terraform | C | **A** | **R** | I | C | I | I |
| Import de l’existant | R | **A** | R | I | C | I | I |
| Approbation des MPE | R (propriétaire cible) | I | I | I | C | I | I |
| Validation des flux et exceptions | R | C | I | C | **A** | C | I |
| DAG des data products | C | I | I | **A/R** | C | I | I |
| Déploiement des items (fabric-cicd) | **R** | C | I | I | I | I | C |
