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
# Banner
# ------------------------------------------------------------------------------
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗"
echo -e "║             ⚡ CREATING SUPERUSER FOR DJANGO ⚡              ║"
echo -e "╚══════════════════════════════════════════════════════════════╝${RESET}\n"

# ------------------------------------------------------------------------------
# Wait for Database
# ------------------------------------------------------------------------------
echo -e "${YELLOW}⏳ Waiting for database to be ready...${RESET}\n"
sleep 2

# ------------------------------------------------------------------------------
# Create Superuser
# ------------------------------------------------------------------------------
echo -e "${CYAN}✨ Attempting to create superuser with Username='admin' and Password='admin123'...${RESET}\n"

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser successfully created.")
else:
    print("Superuser already exists.")
EOF

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Superuser script finished successfully.${RESET}\n"
else
    echo -e "${RED}❌ Failed to create superuser.${RESET}\n"
    exit 1
fi

# ------------------------------------------------------------------------------
# Final Banner
# ------------------------------------------------------------------------------
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║   Superuser Username='admin' and Password='admin123' is now ready!   ║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}\n"

