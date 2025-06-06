#!/bin/bash

# Colors
RED='\033[1;31m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
GREEN='\033[1;32m'
RESET='\033[0m'

# ╔════════════════════════════════════════════════════════════════════════╗
# ║ ⚠️ WARNING: This will flush the database — ALL DATA WILL BE LOST! ⚠️   ║
# ╚════════════════════════════════════════════════════════════════════════╝

echo -e "${RED}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ ⚠️  WARNING: This will flush the database in the server container.      ║"
echo -e "║     ${YELLOW}ALL EXISTING DATA WILL BE LOST. Proceeding with flush...${RED}           ║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"
echo ""

docker exec -it server python manage.py flush --no-input

echo -e "${GREEN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ ✅  Flush complete! ${CYAN}Your Django DB is now clean and fresh. 🧼✨       ${GREEN}║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"
