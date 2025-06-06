#!/bin/bash

# Wait for DB to be ready (optional but useful)
echo "Waiting for database..."
sleep 5

echo "Creating superuser..."

# Run Django command to create superuser only if it doesn't exist
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF
