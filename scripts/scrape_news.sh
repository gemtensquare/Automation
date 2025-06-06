#!/bin/bash


echo "🔍 Hitting /api/news/scrape/..."
for i in {1..10}; do
  if curl -sSf http://127.0.0.1:8000/api/news/scrape/; then
    echo -e "\n✅ Scraping triggered successfully!"
    if curl -sSf http://127.0.0.1:8000/api/redis/clear/; then
      echo -e "\n✅ Redis cache cleared successfully!"
      exit 0
    fi
  else
    echo "⚠️ Attempt $i: Scrape endpoint not responding. Retrying in 10s..."
    sleep 10
  fi
done

echo "❌ Scrape endpoint failed after multiple attempts."
exit 1
