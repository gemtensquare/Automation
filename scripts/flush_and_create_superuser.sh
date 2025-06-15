#! /bin/bash

# ------------------------------------------------------------------------------
# Colors
# ------------------------------------------------------------------------------
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[1;31m'
RESET='\033[0m'

# ------------------------------------------------------------------------------
# WARNING Banner
# ------------------------------------------------------------------------------
echo -e "${RED}╔══════════════════════════════════════════════════════════════════════════════╗"
echo -e "║ ⚡ WARNING: This will FLUSH the database in your server container.           ║"
echo -e "║          ${YELLOW}ALL EXISTING DATA WILL BE LOST. Proceeding with FLUSH!${RED}              ║"
echo -e "╚══════════════════════════════════════════════════════════════════════════════╝${RESET}\n"

# ------------------------------------------------------------------------------
# Perform Flush
# ------------------------------------------------------------------------------
echo -e "${YELLOW}Flushing the database...${RESET}"
docker compose exec -it server python manage.py flush --noinput

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Database successfully flushed.${RESET}"
else
    echo -e "${RED}❌ Failed to flush the database.${RESET}"
    exit 1
fi

# ------------------------------------------------------------------------------
# Create Superuser
# ------------------------------------------------------------------------------
echo -e "${CYAN}Creating a new superuser with Username='admin' and Password='admin'...${RESET}"

docker compose exec -it server python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Superuser successfully created.${RESET}"
else
    echo -e "${RED}❌ Failed to create a superuser.${RESET}"
    exit 1
fi

# ------------------------------------------------------------------------------
# Final Banner
# ------------------------------------------------------------------------------
echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════════════════════╗"
echo -e "║✅ All done! Superuser with Username='admin' and Password='admin' successfully!    ║"
echo -e "╚═══════════════════════════════════════════════════════════════════════════════════╝${RESET}\n"

