#!/bin/bash

echo "⏳ Final check news: wait for 5 seconds..."
sleep 5

echo "🔍 Checking final news list at /api/news/..."
for i in {1..10}; do
  if curl -sSf http://127.0.0.1:8000/api/news/; then
    echo "✅ News list is available!"
    exit 0
  else
    echo "⚠️ Attempt $i: News list not responding. Retrying in 10s..."
    sleep 10
  fi
done

echo "❌ News list failed to respond after multiple attempts."
exit 1
