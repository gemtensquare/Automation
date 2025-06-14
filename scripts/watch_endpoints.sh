#!/bin/bash

# Watch endpoints
echo -e "\033[1;36m⚙️ Running watch_endpoints.sh...\033[0m"
echo "Repo: $REPO"

echo -e "\033[1;34m🔐 Making all scripts in ./scripts executable...\033[0m"
chmod +x ./scripts/*.sh

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
  # redis_response=$(curl -sSf http://127.0.0.1:8000/api/redis/)
  # if [[ $? -eq 0 ]]; then
  #   # Show full raw response
  #   echo -e "\n${CYAN}📤 Redis /api/redis/ Cache Full Response:${RESET}"
  #   echo -e "${GREEN}$redis_response${RESET}"
  # else
  #   echo -e "${RED}⚠️  Redis API request failed. Skipping Redis block.${RESET}"
  # fi

  if (( i % 4 == 0 )); then
    echo -e "\n${CYAN}📂 Latest update from ${MAGENTA}news_scraping_log.txt:${RESET}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
    tail -n 5 logs/news_scraping_log.txt 2>/dev/null || echo -e "${RED}⚠️  File not found or inaccessible.${RESET}"
    # echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

    echo -e "\n${CYAN}📂 Latest update from ${MAGENTA}news_posted_log.txt:${RESET}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
    tail -n 5 logs/news_posted_log.txt 2>/dev/null || echo -e "${RED}⚠️  File not found or inaccessible.${RESET}"
    # echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
  fi

  if (( i % 12 == 0 )); then
    echo -e "\033[1;36m⚙️ Running database backup script: backup_GemtenAi_db.sh...\033[0m"
    sh ./scripts/backup_GemtenAi_db.sh

    # Set timezone to UTC+6 (Dhaka)
    export TZ="Asia/Dhaka"
    NOW=$(date +"%d %B %Y - %I:%M %p")

    echo -e "\033[1;34m🌏 Timezone set to Asia/Dhaka (UTC+6)\033[0m"
    echo -e "\033[1;32m📅 Current date & time: $NOW\033[0m"

    # Configure git user
    echo -e "\033[1;33m🔧 Configuring Git user...\033[0m"
    git config user.name "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # pull changes
    echo -e "\033[1;33m📡 Pulling changes from GitHub...\033[0m"
    git pull

    # Make change
    echo -e "\033[1;36m📝 Appending timestamp to auto_backup_and_push_log.txt...\033[0m"
    echo "Backup database and Push update at $NOW" >> logs/auto_backup_and_push_log.txt

    # Commit changes
    echo -e "\033[1;33m💾 Creating commit...\033[0m"
    git add .
    git commit -m "Backup database at $NOW" || echo -e "\033[1;90m⚠️ No changes to commit\033[0m"

    # Push changes using PAT token
    echo -e "\033[1;35m🚀 Pushing changes to GitHub...\033[0m"
    git push https://x-access-token:${TOKEN}@github.com/${REPO}.git HEAD:main && \
    echo -e "\033[1;32m✅ Push completed successfully!\033[0m" || \
    echo -e "\033[1;31m❌ Push failed! Please check your token and permissions.\033[0m"
  fi

  if (( i == 70 )); then
    echo -e "\033[1;36m⚙️ Running database backup script: backup_GemtenAi_db.sh...\033[0m"
    sh ./scripts/backup_GemtenAi_db.sh

    # Set timezone to UTC+6 (Dhaka)
    export TZ="Asia/Dhaka"
    NOW=$(date +"%d %B %Y - %I:%M %p")

    echo -e "\033[1;34m🌏 Timezone set to Asia/Dhaka (UTC+6)\033[0m"
    echo -e "\033[1;32m📅 Current date & time: $NOW\033[0m"

    # Configure git user
    echo -e "\033[1;33m🔧 Configuring Git user...\033[0m"
    git config user.name "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # Make change
    echo -e "\033[1;36m📝 Appending timestamp to pushed.txt...\033[0m"
    echo "Backup database and Push update at $NOW" >> logs/auto_backup_and_push_log.txt

    # Commit changes
    echo -e "\033[1;33m💾 Creating commit...\033[0m"
    git add .
    git commit -m "Backup database at $NOW" || echo -e "\033[1;90m⚠️ No changes to commit\033[0m"

    # Push changes using PAT token
    echo -e "\033[1;35m🚀 Pushing changes to GitHub...\033[0m"
    git push https://x-access-token:${TOKEN}@github.com/${REPO}.git HEAD:main && \
    echo -e "\033[1;32m✅ Push completed successfully!\033[0m" || \
    echo -e "\033[1;31m❌ Push failed! Please check your token and permissions.\033[0m"
    # Number of times to trigger the workflow
    TIMES=1

    echo "🚀 Triggering CI Workflow $TIMES times..."
    echo ""

    for (( i=1; i<=TIMES; i++ ))
    do
      echo "🔄 Triggering CI run #$i"
      echo ""
      echo ""
      curl -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $TOKEN" \
        https://api.github.com/repos/${REPO}/actions/workflows/run_docker_news_app.yml/dispatches \
        -d '{"ref":"main"}'
      
      echo "✅ Trigger $i sent."
      
      echo "Wait 5 seconds between triggers to avoid hitting rate limits"
      echo ""
      sleep 5
    done

    echo -e "🎉 New Workflow Started! 🕒 Stop the Runner at $(TZ='Asia/Dhaka' date '+%I:%M %p, %d %B %Y')"
    exit 0
  fi

  sleep $INTERVAL_SECONDS
done
