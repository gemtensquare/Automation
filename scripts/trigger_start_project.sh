#!/bin/bash


# Number of times to trigger the workflow
TIMES=3

echo "🚀 Triggering CI Workflow $TIMES times..."
echo ""

for (( i=1; i<=TIMES; i++ ))
do
  echo "🔄 Triggering CI run #$i"
  curl -X POST \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $TOKEN" \
    https://api.github.com/repos/${REPO}/actions/workflows/ci.yml/dispatches \
    -d '{"ref":"main"}'
  
  echo "✅ Trigger $i sent."
  
  echo "Wait 10 seconds between triggers to avoid hitting rate limits"
  echo ""
  sleep 10
done

echo "🎉 All $TIMES workflow triggers sent!"
