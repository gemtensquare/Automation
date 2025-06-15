from bs4 import BeautifulSoup
import requests, os, random, time
from django.utils import timezone
from django.core.cache import cache
from django.core.files.base import ContentFile


from .helpers import Helper
from News.models import News
from . import constants

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

class Scraping:
    def test():
        print("test")
        pass

    
    def save_news(title, intro, category, news_url, image_url, source="", type="bn"):
        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            print('*** skipping for image')
            return

        filename = Helper.get_a_unique_image_name()
        news_obj = News.objects.create(
            title=title, intro=intro, category=category, type=type,
            url=news_url, image_url=image_url, source=source,
        )
        news_obj.image.save(filename, ContentFile(image_response.content), save=True)
        
        return news_obj



    def scrape_khela(topic, category=None):
        added_news_ids = []
        url = 'https://khela.com/' + topic
        res = requests.get(url=url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        cards = soup.select(".items-stretch")
        for card in cards:
            link_tag = card.select_one("a")
            img_tag = card.select_one("img")
            title_tag = card.select_one("h3")
            intro_tag = card.select_one("h3")

            news_url = link_tag['href'] if link_tag else None
            title = title_tag.text.strip() if title_tag else None
            intro = intro_tag.text.strip() if intro_tag else None
            image_url = img_tag['src']

            if not title or not news_url or News.objects.filter(title=title, url=news_url):
                print('*** skipping')
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                print('*** skipping for image')
                continue
            
            filename = Helper.get_a_unique_image_name()

            news_obj = News.objects.create(
                title=title, category=category, type="bn", intro=intro,
                url=news_url, image_url=image_url, source="khela.com", 
            )
            news_obj.image.save(filename, ContentFile(image_response.content), save=True)
            added_news_ids.append(news_obj.id)
        return added_news_ids


    def scrape_jugantor(topic, category=None):
        response = []
        url = 'https://www.jugantor.com/' + topic
        res = requests.get(url=url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        cards = soup.select(".media.positionRelative.marginB5")
        for card in cards:
            title_tag = card.select_one("h4")
            intro_tag = card.select_one("p")
            link_tag = card.select_one("a.linkOverlay")
            img_tag = card.select_one("img")

            title = title_tag.text.strip() if title_tag else None
            intro = intro_tag.text.strip() if intro_tag else None
            news_url = link_tag['href'] if link_tag else None
            image_url =  Helper.process_jugantor_image_url(img_tag['data-src'])

            if not title or not news_url or News.objects.filter(title=title, url=news_url):
                print('*** skipping')
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                print('*** skipping for image')
                continue
            
            filename = Helper.get_a_unique_image_name()

            news_obj = News.objects.create(
                title=title, category=category, type="bn", intro=intro,
                url=news_url, image_url=image_url, source="jugantor.com", 
            )
            news_obj.image.save(filename, ContentFile(image_response.content), save=True)
            response.append(news_obj.id)
        return response
    
    
    def scrape_bd_pratidin(topic, category=None):
        response = []
        url = 'https://www.bd-pratidin.com/' + topic
        res = requests.get(url=url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        cards = soup.select(".col-6.col-lg-4.col-xl-3.mb-3") + soup.select(".col-6.my-3")
        for card in cards:
            title_tag = card.select_one("h5")
            link_tag = card.select_one("a.stretched-link")
            img_tag = card.select_one("img")

            title = title_tag.text.strip() if title_tag else None
            news_url = link_tag['href'] if link_tag else None
            image_url =  Helper.process_bd_protidin_image_url(img_tag['src'])

            if not title or not news_url or News.objects.filter(title=title, url=news_url):
                print('*** skipping')
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                print('*** skipping for image')
                continue
            
            filename = Helper.get_a_unique_image_name()

            news_obj = News.objects.create(
                title=title, category=category, type="bn",
                url=news_url, image_url=image_url, source="bd-pratidin.com", 
            )
            news_obj.image.save(filename, ContentFile(image_response.content), save=True)
            response.append(news_obj.id)
        return response
    
    
    def scrape_bbc_bangla(topic, category=None):
        response = []
        url = 'https://www.bbc.com/bengali/topics/' + topic
        res = requests.get(url=url, headers=HEADERS, timeout=10)

        soup = BeautifulSoup(res.text, 'html.parser')
        all_news = soup.select('.bbc-t44f9r')

        for news in all_news:
            soup = BeautifulSoup(str(news), 'html.parser')
            ref = soup.find('a')
            img = soup.find('img')

            title = ref.get_text()
            news_url = ref['href']
            image_url = Helper.process_bbc_news_image_url(img['src'])

            if not title or not news_url or News.objects.filter(title=title, url=news_url):
                print('*** skipping')
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                print('*** skipping for image')
                continue
            
            filename = Helper.get_a_unique_image_name()

            news_obj = News.objects.create(
                title=title, category=category, type="bn",
                url=news_url, image_url=image_url, source="bbc.com", 
            )
            news_obj.image.save(filename, ContentFile(image_response.content), save=True)
            response.append(news_obj.id)
        return response


    def scrape_daily_star(topic, category=None):
        response = []
        base_url = 'https://www.thedailystar.net/'
        base_url = 'https://bangla.thedailystar.net/'
        url = base_url + topic
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')

                cards = soup.select('.card.position-relative.horizontal')
                for card in cards:
                    try:
                        source_tag = card.select_one('source')
                        image_url = Helper.process_dayli_start_news_image_url(source_tag['data-srcset']) if source_tag and source_tag.has_attr('data-srcset') else ''
                        
                        content = card.select_one('.card-content')
                        if not content:
                            continue

                        title_tag = content.select_one('h3.title a')
                        title = title_tag.text.strip() if title_tag else ''
                        news_url = base_url + title_tag['href'] if title_tag else ''

                        intro_tag = content.select_one('p.intro')
                        intro = intro_tag.text.strip() if intro_tag else ''

                        if not image_url or not title or not news_url or News.objects.filter(title=title, url=news_url):
                            print('*** skipping')
                            continue

                        news_obj = Scraping.save_news(title, intro, category, news_url, image_url, source="bangla.thedailystar.net")
                        response.append(news_obj.id)
                        
                    except Exception as inner_e:
                        print(f"Error parsing a card: {inner_e}")
            else:
                print(f"Request failed with status code {res.status_code}")
        except Exception as e:
            print(f"The Daily Star error: {e}")
        return response
    

    def scrape_jagonews24(topic, category=None):
        response = []
        base_url = 'https://www.jagonews24.com/'
        url = base_url + topic
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')

                cards = soup.select(".single-block.cat-block")
                for card in cards:
                    try:
                        link_tag = card.select_one("a")
                        img_tag = card.select_one("img")
                        title_tag = card.select_one("h3 a")

                        # Extracting data
                        news_url = link_tag['href'] if link_tag else None
                        title = title_tag.text.strip() if title_tag else None

                        # Use data-src for actual image; fallback to src
                        raw_image_url = img_tag.get('data-src') or img_tag.get('src')
                        image_url = Helper.process_jagonews24_news_image_url(raw_image_url)

                        if not image_url or not title or not news_url or News.objects.filter(title=title, url=news_url):
                            print('*** skipping')
                            continue

                        news_obj = Scraping.save_news(title, title, category, news_url, image_url, source="jagonews24.com")
                        response.append(news_obj.id)
                        
                    except Exception as inner_e:
                        print(f"Error parsing a card: {inner_e}")
            else:
                print(f"Request failed with status code {res.status_code}")
        except Exception as e:
            print(f"The Daily Star error: {e}")
        return response
    
    def scrape_bdcrictime(topic, category=None):
        response = []
        base_url = 'https://bn.bdcrictime.com'
        url = base_url + topic
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')

                cards = soup.select(".post2")
                for card in cards:
                    try:
                        # Title and link
                        link_tag = card.select_one(".content a")
                        title = link_tag.text.strip() if link_tag else "None"
                        news_url = base_url + link_tag['href'] if link_tag and link_tag.has_attr('href') else "None"

                        # Image
                        img_tag = card.select_one("img")
                        raw_image_url = img_tag.get('data-src') or img_tag.get('src') if img_tag else None
                        image_url = raw_image_url

                        if not image_url or not title or not news_url or News.objects.filter(title=title, url=news_url):
                            print('*** skipping')
                            continue

                        news_obj = Scraping.save_news(title, title, category, news_url, image_url, source="bdcrictime.com")
                        response.append(news_obj.id)
                        
                    except Exception as inner_e:
                        print(f"Error parsing a card: {inner_e}")
            else:
                print(f"Request failed with status code {res.status_code}")
        except Exception as e:
            print(f"The Daily Star error: {e}")
        return response
    

    def scrape_all_khela_news():
        Cricket_news_ids = Scraping.scrape_khela('cricket', 'Cricket')
        Football_news_ids = Scraping.scrape_khela('football', 'Football')

        news_ids = Cricket_news_ids + Football_news_ids
        Helper.log_scraping_news('Khela', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_CRICKET_PAGE_ID, Cricket_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_FOOTBALL_PAGE_ID, Football_news_ids)
        return news_ids
    

    def scrape_all_jagonews24_news():
        news_ids = []

        Cricket_news_ids = Scraping.scrape_jagonews24('sports/cricket', 'Cricket')
        Football_news_ids = Scraping.scrape_jagonews24('sports/football', 'Football')
        Entertainment_news_ids = Scraping.scrape_jagonews24('entertainment/hollywood', 'Entertainment')
        Entertainment_news_ids += Scraping.scrape_jagonews24('entertainment/bollywood', 'Entertainment')

        news_ids += Cricket_news_ids + Football_news_ids + Entertainment_news_ids
        Helper.log_scraping_news('Jagonews24', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_CRICKET_PAGE_ID, Cricket_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_FOOTBALL_PAGE_ID, Football_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_ShowBiz_PAGE_ID, Entertainment_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Cricket_news_ids + Football_news_ids)
        return news_ids

    def scrape_all_jugantor_news():
        news_ids = []
        news_ids += Scraping.scrape_jugantor('health', 'Health')
        news_ids += Scraping.scrape_jugantor('economics', 'Economy')
        news_ids += Scraping.scrape_jugantor('politics', 'Politics')
        news_ids += Scraping.scrape_jugantor('business', 'Business')

        Sports_news_ids = Scraping.scrape_jugantor('sports', 'Sports')
        Technology_news_ids = Scraping.scrape_jugantor('technology', 'Technology')
        Entertainment_news_ids = Scraping.scrape_jugantor('entertainment', 'Entertainment')

        news_ids += Technology_news_ids + Entertainment_news_ids + Sports_news_ids

        Helper.log_scraping_news('Jugantor', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Sports_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_TERABYTE_PAGE_ID, Technology_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_ShowBiz_PAGE_ID, Entertainment_news_ids)
        return news_ids
    
    def scrape_all_bd_pratidin_news():
        news_ids = []
        news_ids += Scraping.scrape_bd_pratidin('islam', 'Islam')
        news_ids += Scraping.scrape_bd_pratidin('science', 'Science')
        news_ids += Scraping.scrape_bd_pratidin('economy', 'Economy')
        news_ids += Scraping.scrape_bd_pratidin('national', 'National')
        news_ids += Scraping.scrape_bd_pratidin('health-tips', 'Health')
        news_ids += Scraping.scrape_bd_pratidin('city-news', 'City News')
        news_ids += Scraping.scrape_bd_pratidin('minister-spake', 'Politics')

        Sports_news_ids = Scraping.scrape_bd_pratidin('sports', 'Sports')
        Entertainment_news_ids = Scraping.scrape_bd_pratidin('entertainment', 'Entertainment')

        news_ids += Entertainment_news_ids + Sports_news_ids
        Helper.log_scraping_news('BD Pratidin', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Sports_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_ShowBiz_PAGE_ID, Entertainment_news_ids)
        return news_ids
    
    def scrape_all_bbc_bangla_news():
        news_ids = []
        news_ids += Scraping.scrape_bbc_bangla('c907347rezkt', 'World')
        news_ids += Scraping.scrape_bbc_bangla('cg7265yyxn1t', 'Health')
        news_ids += Scraping.scrape_bbc_bangla('cjgn7233zk5t', 'Economy')
        news_ids += Scraping.scrape_bbc_bangla('cqywj91rkg6t', 'Politics')
        
        Sports_news_ids = Scraping.scrape_bbc_bangla('cdr56g57y01t', 'Sports')
        Technology_news_ids = Scraping.scrape_bbc_bangla('c8y94k95v52t', 'Technology')

        news_ids += Technology_news_ids + Sports_news_ids
        Helper.log_scraping_news('BBC Bangla', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Sports_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_TERABYTE_PAGE_ID, Technology_news_ids)
        return news_ids
    
    def scrape_all_daily_star_news():
        news_ids = []
        news_ids += Scraping.scrape_daily_star('health', 'Health')
        news_ids += Scraping.scrape_daily_star('abroad', 'Abroad')
        news_ids += Scraping.scrape_daily_star('business', 'Business')

        Sports_news_ids = Scraping.scrape_daily_star('sports', 'Sports')
        Technology_news_ids = Scraping.scrape_daily_star('tech-startup', 'Technology')
        Education_news_ids = Scraping.scrape_daily_star('youth/education', 'Education')
        Entertainment_news_ids = Scraping.scrape_daily_star('entertainment', 'Entertainment')

        news_ids += Entertainment_news_ids + Education_news_ids + Technology_news_ids + Sports_news_ids
        
        Helper.log_scraping_news('Daily Star', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Sports_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_TERABYTE_PAGE_ID, Technology_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_ShowBiz_PAGE_ID, Entertainment_news_ids)
        return news_ids
    
    def scrape_all_bdcrictime_news():
        news_ids = []

        Sports_news_ids = Scraping.scrape_bdcrictime('/news', 'Cricket')

        news_ids += Sports_news_ids
        
        Helper.log_scraping_news('BD CricTime', news_ids=news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_NEWS_PAGE_ID, news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_SPORTS_PAGE_ID, Sports_news_ids)
        Helper.set_queue_news_to_page(constants.GEMTEN_CRICKET_PAGE_ID, Sports_news_ids)
        return news_ids
    
    def scrape_all_news():
        news_ids = []
        news_ids += Scraping.scrape_all_khela_news()
        news_ids += Scraping.scrape_all_jugantor_news()
        news_ids += Scraping.scrape_all_bdcrictime_news()
        news_ids += Scraping.scrape_all_bdcrictime_news()
        news_ids += Scraping.scrape_all_jagonews24_news()
        news_ids += Scraping.scrape_all_bbc_bangla_news()
        news_ids += Scraping.scrape_all_daily_star_news()
        news_ids += Scraping.scrape_all_bd_pratidin_news()
        return news_ids
    

    def _scrape_all__news():
        news_ids = []
        return news_ids

