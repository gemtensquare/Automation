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
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
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
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
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
                continue

            image_response = requests.get(image_url)
            if image_response.status_code != 200:
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
        url = base_url + topic
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                # Select all cards inside .view-content
                for card in soup.select('.card.position-relative.horizontal'):
                    try:
                        image_url = Helper.process_dayli_start_news_image_url(card.select_one('source')['data-srcset'])
                        
                        card = card.select_one('.card-content')

                        title = card.select_one('a').text.strip()
                        news_url = base_url + card.select_one('a')['href']
                        if not title or not news_url or News.objects.filter(title=title, url=news_url):
                            continue

                        intro = card.select_one('.intro').text.strip() if card.select_one('.intro') else ''
                        image_url = image_url.replace(' 1x', '')

                        image_response = requests.get(image_url)
                        if image_response.status_code != 200:
                            continue

                        filename = Helper.get_a_unique_image_name()
                        news_obj = News.objects.create(
                            title=title, intro=intro, category=category, 
                            url=news_url, image_url=image_url, source="thedailystar.net",
                        )
                        news_obj.image.save(filename, ContentFile(image_response.content), save=True)
                        response.append(news_obj.id)
                    except Exception as inner_e:
                        print(f"Error parsing a card: {inner_e}")
            else:
                print(f"Request failed with status code {res.status_code}")
        except Exception as e:
            print(f"The Daily Star error: {e}")
        print('%'*30, response)
        return response
    

    def scrape_all_jugantor_news():
        news_ids = []
        news_ids += Scraping.scrape_jugantor('sports', 'Sports')
        news_ids += Scraping.scrape_jugantor('health', 'Health')
        news_ids += Scraping.scrape_jugantor('economics', 'Economy')
        news_ids += Scraping.scrape_jugantor('politics', 'Politics')
        news_ids += Scraping.scrape_jugantor('business', 'Business')
        news_ids += Scraping.scrape_jugantor('technology', 'Technology')
        news_ids += Scraping.scrape_jugantor('entertainment', 'Entertainment')

        Helper.log_scraping_news('Jugantor', news_ids=news_ids)

        return news_ids
    
    def scrape_all_bd_pratidin_news():
        news_ids = []
        news_ids += Scraping.scrape_bd_pratidin('islam', 'Islam')
        news_ids += Scraping.scrape_bd_pratidin('sports', 'Sports')
        news_ids += Scraping.scrape_bd_pratidin('science', 'Science')
        news_ids += Scraping.scrape_bd_pratidin('economy', 'Economy')
        news_ids += Scraping.scrape_bd_pratidin('national', 'National')
        news_ids += Scraping.scrape_bd_pratidin('health-tips', 'Health')
        news_ids += Scraping.scrape_bd_pratidin('city-news', 'City News')
        news_ids += Scraping.scrape_bd_pratidin('minister-spake', 'Politics')
        news_ids += Scraping.scrape_bd_pratidin('entertainment', 'Entertainment')

        Helper.log_scraping_news('BD Pratidin', news_ids=news_ids)

        return news_ids
    
    def scrape_all_bbc_bangla_news():
        news_ids = []
        news_ids += Scraping.scrape_bbc_bangla('c907347rezkt', 'World')
        news_ids += Scraping.scrape_bbc_bangla('cg7265yyxn1t', 'Health')
        news_ids += Scraping.scrape_bbc_bangla('cdr56g57y01t', 'Sports')
        news_ids += Scraping.scrape_bbc_bangla('cjgn7233zk5t', 'Economy')
        news_ids += Scraping.scrape_bbc_bangla('cqywj91rkg6t', 'Politics')
        news_ids += Scraping.scrape_bbc_bangla('c8y94k95v52t', 'Technology')

        Helper.log_scraping_news('BBC Bangla', news_ids=news_ids)

        return news_ids
    
    def scrape_all_daily_star_news():
        news_ids = []
        news_ids += Scraping.scrape_daily_star('sports', 'Sports')
        news_ids += Scraping.scrape_daily_star('business', 'Business')
        news_ids += Scraping.scrape_daily_star('tech-startup', 'TechStartup')
        news_ids += Scraping.scrape_daily_star('news/bangladesh', 'Bangladesh')
        news_ids += Scraping.scrape_daily_star('entertainment', 'Entertainment')

        Helper.log_scraping_news('Daily Star', news_ids=news_ids)

        return news_ids
    
    def scrape_all_news():
        news_ids = []
        news_ids += Scraping.scrape_all_bbc_bangla_news()
        news_ids += Scraping.scrape_all_bd_pratidin_news()
        news_ids += Scraping.scrape_all_daily_star_news()
        news_ids += Scraping.scrape_all_jugantor_news()
        return news_ids
    

    def scrape_all__news():
        news_ids = []
        return news_ids

