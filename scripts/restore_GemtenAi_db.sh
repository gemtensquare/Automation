#!/bin/bash

# Colors
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
GREEN='\033[1;32m'
MAGENTA='\033[1;35m'
RESET='\033[0m'

# ╔══════════════════════════════════════════════════════╗
# ║ 🔄 Restoring GemtenAi_db with a sprinkle of magic! ✨ ║
# ╚══════════════════════════════════════════════════════╝


echo -e "${CYAN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ 🔄 ${YELLOW}Starting to restore GemtenAi_db from dump.sql...${CYAN} 🚀                 ║"
echo -e "║    ${MAGENTA}Restoring every byte with love and care. 🐢💖                      ${CYAN}║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"
echo ""

docker exec -i postgres psql -U postgres -d GemtenAi_db < dump.sql

echo -e "\n\n\n"
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ 🎉 Restore complete! ${YELLOW}GemtenAi_db is back in action!${GREEN} ✨💕               ║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"

