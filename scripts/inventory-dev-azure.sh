#!/usr/bin/env bash
# ==============================================================================
# inventory-dev-azure.sh — inventaire Azure de l’environnement DEV, LECTURE SEULE
#
# Ce script n’exécute QUE des commandes « az … list » et « az … show ».
# Il ne modifie, ne crée, ne supprime et n’approuve aucune ressource.
# Il ne lit JAMAIS la valeur d’un secret : les secrets du Key Vault sont listés
# par nom et métadonnées (az keyvault secret list), jamais avec « secret show ».
#
# Prérequis : az login (compte personnel, rôle Reader suffisant), jq.
# Usage    : ./inventory-dev-azure.sh [dossier_de_sortie]
# Sortie   : JSON bruts dans <sortie>/raw, synthèse dans <sortie>/summary.txt
# ==============================================================================
set -euo pipefail

# --- Valeurs CONFIRMÉES (exports fournis) ---------------------------------------
SUBSCRIPTION_ID="0c53c37e-2ed2-4d58-b147-8f80763294ce"   # FR-AZR-DP-DEV
RG="frappdevdp0001"
VNET="fralzvnetdev1055"
KV="frfrkvdevdp0001"
ROUTE_TABLE="fr_rt_fralzvnetdev1055"
# Zone DNS privée Fabric du hub (souscription fr-connectivity, gérée par Terraform) — lecture seule
DNS_SUB="1fe4e122-3c20-4707-88ed-3ce3fa2e259f"
DNS_RG="frinfalzconnectivityprivatedns0001"
DNS_ZONE="privatelink.fabric.microsoft.com"

OUT="${1:-./inventory-dev-$(date +%Y%m%d-%H%M%S)}"
RAW="$OUT/raw"
mkdir -p "$RAW"

# Garde-fou : refuse toute sous-commande qui n’est pas list/show/get
run() {
  local name="$1"; shift
  case " $* " in
    *" list "*|*" show "*|*" list-"*|*" get "*) ;;
    *) echo "REFUS : commande non autorisée (lecture seule) : az $*" >&2; exit 2 ;;
  esac
  case " $* " in
    *" secret show "*|*" secret download "*|*"--show-secret"*) echo "REFUS : lecture de secret interdite" >&2; exit 2 ;;
  esac
  echo "-> az $*"
  if ! az "$@" --only-show-errors -o json > "$RAW/$name.json" 2> "$RAW/$name.err"; then
    echo "   ! échec (droits insuffisants ?) — voir $RAW/$name.err"
  else
    rm -f "$RAW/$name.err"
  fi
}

command -v az >/dev/null || { echo "az CLI requis"; exit 1; }
command -v jq >/dev/null || { echo "jq requis"; exit 1; }

run account                 account show
az account set --subscription "$SUBSCRIPTION_ID"   # sélection de contexte local, sans effet sur Azure

# --- Socle -----------------------------------------------------------------------
run resource-group          group show --name "$RG"
run resources               resource list --resource-group "$RG"
run fabric-pls              resource list --resource-type Microsoft.Fabric/privateLinkServicesForFabric
run fabric-capacities       resource list --resource-type Microsoft.Fabric/capacities

# --- Réseau -----------------------------------------------------------------------
run vnet                    network vnet show --resource-group "$RG" --name "$VNET"
run subnets                 network vnet subnet list --resource-group "$RG" --vnet-name "$VNET"
run peerings                network vnet peering list --resource-group "$RG" --vnet-name "$VNET"
run route-table             network route-table show --resource-group "$RG" --name "$ROUTE_TABLE"
run routes                  network route-table route list --resource-group "$RG" --route-table-name "$ROUTE_TABLE"
run private-endpoints       network private-endpoint list --resource-group "$RG"
run nics                    network nic list --resource-group "$RG"
run private-dns-zones       network private-dns zone list
run nsg                     network nsg list --resource-group "$RG"

# --- Zone DNS privée du hub (Reader requis sur fr-connectivity ; échec toléré) ------
run dns-zone-fabric         network private-dns zone show --subscription "$DNS_SUB" --resource-group "$DNS_RG" --name "$DNS_ZONE"
run dns-zone-vnet-links     network private-dns link vnet list --subscription "$DNS_SUB" --resource-group "$DNS_RG" --zone-name "$DNS_ZONE"
run dns-zone-a-records      network private-dns record-set a list --subscription "$DNS_SUB" --resource-group "$DNS_RG" --zone-name "$DNS_ZONE"

# --- Key Vault (métadonnées uniquement) ------------------------------------------
run keyvault                keyvault show --name "$KV"
run keyvault-secrets-meta   keyvault secret list --vault-name "$KV"
run keyvault-pe-conn        network private-endpoint-connection list --resource-group "$RG" --name "$KV" --type Microsoft.KeyVault/vaults

# --- Identités (sans secret) -------------------------------------------------------
run role-assignments-rg     role assignment list --resource-group "$RG" --include-inherited

# --- Assainissement ---------------------------------------------------------------
# Supprime de la sortie tout champ susceptible de contenir une valeur secrète
for f in "$RAW"/*.json; do
  [ -s "$f" ] || continue
  jq 'walk(if type == "object" then with_entries(select(.key | test("^(value|secret|password|clientSecret|primaryKey|secondaryKey|connectionString)$"; "i") | not)) else . end)' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done

# --- Synthèse ---------------------------------------------------------------------
{
  echo "Inventaire DEV — $(date -Iseconds)"
  echo "Souscription : $(jq -r '.name + " (" + .id + ")"' "$RAW/account.json" 2>/dev/null)"
  echo "Ressources du RG : $(jq 'length' "$RAW/resources.json" 2>/dev/null)"
  echo "Private Endpoints : $(jq 'length' "$RAW/private-endpoints.json" 2>/dev/null)"
  echo "IP privées (NIC) : $(jq '[.[].ipConfigurations[]] | length' "$RAW/nics.json" 2>/dev/null)"
  echo "Private Link Fabric (tenant visible) : $(jq 'length' "$RAW/fabric-pls.json" 2>/dev/null)"
  echo "Zone DNS Fabric : $(jq -r '.numberOfRecordSets // "n/a"' "$RAW/dns-zone-fabric.json" 2>/dev/null) recordsets (86 au 08/11/2026), liens VNet : $(jq 'length' "$RAW/dns-zone-vnet-links.json" 2>/dev/null)"
  echo "Secrets Key Vault (noms) :"
  jq -r '.[] | "  - " + .name + "  expire=" + ((.attributes.expires // "n/a")|tostring)' "$RAW/keyvault-secrets-meta.json" 2>/dev/null || true
  echo "Private Endpoints et statut de connexion :"
  jq -r '.[] | "  - " + .name + " : " + ((.privateLinkServiceConnections[0].privateLinkServiceConnectionState.status // .manualPrivateLinkServiceConnections[0].privateLinkServiceConnectionState.status // "?")|tostring)' "$RAW/private-endpoints.json" 2>/dev/null || true
} > "$OUT/summary.txt"

echo "Terminé. Comparez avec : python3 scripts/validate-manifests.py --compare-inventory $OUT"
