#!/bin/bash

echo "⏳ Waiting 10 seconds for the server to boot..."
sleep 10

echo "🔍 Checking if /api/news/ endpoint is responding..."
for i in {1..20}; do
  if curl -sSf http://127.0.0.1:8000/api/news/; then
    echo -e "\n✅ News endpoint is live!"
    exit 0
  else
    echo - "\n⚠️ Attempt $i: News endpoint not up. Retrying in 5s..."
    sleep 5
  fi
done

echo -e "\n❌ News endpoint failed to respond after multiple attempts."
exit 1
