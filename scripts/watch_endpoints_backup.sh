#!/bin/bash

# 🎨 Colors
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[1;36m'
MAGENTA='\033[1;35m'
RESET='\033[0m'

INTERVAL_SECONDS=300

echo -e "${CYAN}🌐 Whiling Runner: Checking if the /api/news/ and /api/redis/ endpoints are alive...${RESET}"

i=0
while true; do
  ((i++))
  echo -e "\n${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
  echo -e "${YELLOW}\t\t\t\t\t 🔁 \t Attempt $i \t 🔁 ${RESET}"
  echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
  
  # Hit /api/news/
  news_response=$(curl -sSf http://127.0.0.1:8000/api/news/)
  if [[ $? -eq 0 ]]; then
    status=$(echo "$news_response" | grep -o '"status":[^,]*' | cut -d':' -f2 | tr -d ' ')
    count=$(echo "$news_response" | grep -o '"count":[^,]*' | cut -d':' -f2 | tr -d ' ')
    duration=$(echo "$news_response" | grep -o '"response_duration":[^,]*' | cut -d':' -f2 | tr -d ' ')
    message=$(echo "$news_response" | grep -o '"message":"[^"]*"' | cut -d':' -f2- | tr -d '"')

    current_time=$(TZ=Asia/Dhaka date +"%d-%m-%Y %I:%M:%S %p (UTC+6)")
    echo -e "\n${CYAN}📦 News /api/news/ Response:${RESET}"
    echo -e "${MAGENTA}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓${RESET}"
    echo -e "${MAGENTA}${RESET}  🟢 Status             : ${status} ${MAGENTA}                                              ${RESET}"
    # echo -e "${MAGENTA}${RESET}  🔢 Count             : ${count} ${MAGENTA}                              ${RESET}"    
    echo -e "${MAGENTA}${RESET}  ⏱️ Response Duration  : ${duration}s ${MAGENTA}                                          ${RESET}"
    echo -e "${MAGENTA}${RESET}  🕒 Current Time       : ${current_time}       ${MAGENTA}                                ${RESET}"
    echo -e "${MAGENTA}${RESET}  💬 Message            : ${message} ${MAGENTA}                                   ${RESET}"
    echo -e "${MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${RESET}"
  else
    echo -e "${RED}⚠️  Attempt $i: Failed to get news API response.${RESET}"
  fi

  # Hit /api/redis/
  redis_response=$(curl -sSf http://127.0.0.1:8000/api/redis/)
  if [[ $? -eq 0 ]]; then
    # Show full raw response
    echo -e "\n${CYAN}📤 Redis /api/redis/ Cache Full Response:${RESET}"
    echo -e "${GREEN}$redis_response${RESET}"
  else
    echo -e "${RED}⚠️  Redis API request failed. Skipping Redis block.${RESET}"
  fi

  if (( i % 4 == 0 )); then
    echo -e "\n${CYAN}📂 Latest update from ${MAGENTA}news_scraping_log.txt:${RESET}"
    echo -e "${YELLOW}────────────────────────────────────────────────────────────────────────────────────────${RESET}"
    tail -n 10 server/news_scraping_log.txt 2>/dev/null || echo -e "${RED}⚠️  File not found or inaccessible.${RESET}"
    # echo -e "${YELLOW}────────────────────────────────────────────────────────────────────────────────────────${RESET}"

    echo -e "\n${CYAN}📂 Latest update from ${MAGENTA}news_posted_log.txt:${RESET}"
    echo -e "${YELLOW}────────────────────────────────────────────────────────────────────────────────────────${RESET}"
    tail -n 5 server/news_posted_log.txt 2>/dev/null || echo -e "${RED}⚠️  File not found or inaccessible.${RESET}"
    # echo -e "${YELLOW}────────────────────────────────────────────────────────────────────────────────────────${RESET}"
  fi

  sleep $INTERVAL_SECONDS
done
