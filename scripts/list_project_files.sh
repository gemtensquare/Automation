#!/bin/bash

# Color codes
GREEN='\033[0;32m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# Box Header
echo -e "\n${CYAN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║               📜    📁 Minimal Project File Overview 💡                ║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"

# Important Files
# echo -e "\n${YELLOW}📄 \t\t\t Highlighted Files:${RESET}"
# [ -f docker-compose.yml ] && echo -e "  ✅ ${GREEN}docker-compose.yml${RESET}"
# [ -f Dockerfile ] && echo -e "  ✅ ${GREEN}Dockerfile${RESET}"
# [ -f requirements.txt ] && echo -e "  ✅ ${GREEN}requirements.txt${RESET}"
# [ -f .env ] && echo -e "  ✅ ${GREEN}.env${RESET}"
# [ -f manage.py ] && echo -e "  ✅ ${GREEN}manage.py${RESET}"
# [ -d scripts ] && echo -e "  📁 ${BLUE}scripts/${RESET} folder found"
# [ -d app ] && echo -e "  📁 ${BLUE}app/${RESET} folder found"
# [ -d news ] && echo -e "  📁 ${BLUE}news/${RESET} folder found"

# All script files
echo -e "\n${YELLOW}📜 \t\t\t All script files \t\t\t 📜${RESET}"
ls -la scripts/

# Root directory
echo -e "\n${YELLOW}🌿 \t\t\t Root directory content \t\t\t 🌿${RESET}"
ls -la 

# Media folder
echo -e "\n${YELLOW}🖼️ \t\t\t Media folder content \t\t\t 🖼️${RESET}"
ls -ls server/Media

# Media folder (recursive, detailed)
echo -e "\n${YELLOW}🖼️ \t\t Media folder content (recursive) \t\t\t 🖼️${RESET}"
ls -lR server/Media

# Footer
echo -e "\n\n${CYAN}ℹ️  Tip: Use 'ls -la' for the full directory listing.${RESET}"
