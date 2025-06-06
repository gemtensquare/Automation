#!/bin/bash
set -e

echo -e "\033[1;34m🔐 Making all scripts in ./scripts executable...\033[0m"
chmod +x ./scripts/*.sh

echo -e "\033[1;36m⚙️ Running database backup script: backup_GemtenAi_db.sh...\033[0m"
sh ./scripts/backup_GemtenAi_db.sh

# Set timezone to UTC+6 (Dhaka)
export TZ="Asia/Dhaka"
NOW=$(date +"%d %B %Y - %I:%M %p")

echo -e "\033[1;34m🌏 Timezone set to Asia/Dhaka (UTC+6)\033[0m"
echo -e "\033[1;32m📅 Current date & time: $NOW\033[0m"

# Configure git user
echo -e "\033[1;33m🔧 Configuring Git user...\033[0m"
# git config user.name "github-actions[bot]"
# git config user.email "github-actions[bot]@users.noreply.github.com"

# Make change
echo -e "\033[1;36m📝 Appending timestamp to pushed.txt...\033[0m"
echo "Pushed at $NOW" >> pushed.txt

# Commit changes
echo -e "\033[1;33m💾 Creating commit...\033[0m"
git add .
git commit -m "Auto commit at $NOW" || echo -e "\033[1;90m⚠️ No changes to commit\033[0m"

# Push changes using PAT token
echo -e "\033[1;35m🚀 Pushing changes to GitHub...\033[0m"
git push https://x-access-token:${TOKEN}@github.com/${REPO}.git HEAD:main && \
echo -e "\033[1;32m✅ Push completed successfully!\033[0m" || \
echo -e "\033[1;31m❌ Push failed! Please check your token and permissions.\033[0m"

# REPO="hELLO"
# TOKEN="YOUR_PAT_TOKEN"

REPO=$REPO TOKEN=$TOKEN sh ./scripts/trigger_start_project.sh