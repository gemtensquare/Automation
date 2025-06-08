#!/bin/bash

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🔄 Starting cron service...${NC}"
service cron start

echo -e "${YELLOW}🧹 Cleaning up existing Django cron jobs...${NC}"
rm -f /server/.crontab
crontab -r || true

echo -e "${YELLOW}➕ Adding new Django cron jobs...${NC}"
python manage.py crontab add
# python manage.py crontab remove
# python manage.py crontab add

echo -e "${YELLOW}⚙️  Running makemigrations...${NC}"
python manage.py makemigrations

echo -e "${YELLOW}📦 Applying database migrations...${NC}"
python manage.py migrate

echo -e "${GREEN}🚀 Starting Django development server at http://0.0.0.0:8000 ...${NC}"
python manage.py runserver 0.0.0.0:8000