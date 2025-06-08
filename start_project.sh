# #!/bin/bash

# # Color codes
# GREEN='\033[0;32m'
# BLUE='\033[0;34m'
# YELLOW='\033[1;33m'
# NC='\033[0m' # No Color

# echo -e "${YELLOW}📦 Starting Docker containers in detached mode...${NC}"
# docker compose up -d

# echo -e "${YELLOW}⏳ Waiting for services to initialize...${NC}"
# sleep 10

# echo -e "${BLUE}🔍 ==================================================================${NC}"
# echo -e "${GREEN}🔍 Checking news endpoint...${NC}"
# sh ./scripts/check_news_endpoint.sh

# echo -e "${BLUE}🔍 ==================================================================${NC}"
# echo -e "${GREEN}📰 Scraping news...${NC}"
# sh ./scripts/scrape_news.sh

# echo -e "${BLUE}🔍 ==================================================================${NC}"
# echo -e "${GREEN}✅ Final check on news list...${NC}"
# sh ./scripts/final_check_news_list.sh

# echo -e "${BLUE}🔚 ==================================================================${NC}"
# echo -e "${GREEN}✅ All tasks completed successfully.${NC}"


echo "Backup database and Push update at $NOW" >> logs/auto_backup_and_push_log.txt
