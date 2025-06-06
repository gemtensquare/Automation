#!/bin/bash

echo "⏳ Waiting 5 seconds before scraping..."
sleep 5

echo "🔍 Hitting /api/news/scrape/..."
for i in {1..10}; do
  if curl -sSf http://127.0.0.1:8000/api/news/scrape/; then
    echo -e "\n✅ Scraping triggered successfully!"
    exit 0
  else
    echo "⚠️ Attempt $i: Scrape endpoint not responding. Retrying in 10s..."
    sleep 10
  fi
done

echo "❌ Scrape endpoint failed after multiple attempts."
exit 1
