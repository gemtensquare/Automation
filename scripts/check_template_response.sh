#!/bin/bash

# Colors
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'

# Base URL of your Django server
BASE_URL="http://127.0.0.1:8000"

# Header
echo -e "\n${CYAN}╔════════════════════════════════════════════════════════════════╗"
echo -e "║ 📦 Final Check: Fetching Templates and Verifying Images ✨     ║"
echo -e "╚════════════════════════════════════════════════════════════════╝${RESET}"

echo -e "${YELLOW}⏳ Please wait... giving the server 5 seconds to get ready...${RESET}"
# sleep 5

# Fetch template JSON
RESPONSE=$(curl -s "$BASE_URL/api/template/")

# Check if status is true
if echo "$RESPONSE" | grep -q '"status":true'; then
    echo -e "\n${GREEN}✅ Template API is working! Received data:${RESET}\n"
    echo "$RESPONSE"

    echo -e "\n${YELLOW}🖼️  Checking each image URL response:${RESET}"

    # Extract image paths using grep and check status code
    echo "$RESPONSE" | grep -oP '"image"\s*:\s*"\K[^"]+' | while read -r img_path; do
        full_url="${BASE_URL}${img_path}"
        echo -ne "🌐 Checking ${full_url}... "
        status_code=$(curl -o /dev/null -s -w "%{http_code}" "$full_url")
        
        if [ "$status_code" = "200" ]; then
            echo -e "${GREEN}✔️  OK${RESET}"
        else
            echo -e "${RED}❌ $status_code${RESET}"
        fi
    done

    exit 0
else
    echo -e "${RED}❌ Template API did not return success.${RESET}"
    exit 1
fi
