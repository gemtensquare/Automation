docker compose up -d


sleep 10
echo "🔍 ******************************************************************"
sh ./scripts/check_news_endpoint.sh
echo "🔍 ******************************************************************"
sh ./scripts/scrape_news.sh
echo "🔍 ******************************************************************"
sh ./scripts/final_check_news_list.sh