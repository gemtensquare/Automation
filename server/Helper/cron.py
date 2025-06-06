from django.utils import timezone

from .helpers import Helper
from Helper.scraping import Scraping

from . import constants
from Facebook.facebook_helper import Facebook

def log_cron_run(job_name: str):
    timestamp = timezone.now()
    with open(constants.CRON_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} — ✨ Yay! [{job_name}] just finished its run! ✨\n\n")
    print(f"{timestamp} — 🌈 [{job_name}] is sparkling now! 🌈")


def my_scheduled_job():
    log_cron_run('Generic Scheduled Job')
    # Add your scheduled task logic here

def my_1_minute_job():
    fb = Facebook(page_id=constants.GEMTEN_NEWS_PAGE_ID, page_access_token=constants.GEMTEN_NEWS_PAGE_ACCESS_TOKEN)
    # fb.post_text_to_page(message=f"New post at {timezone.now()}")
    log_cron_run('1-Minute Job')
    # Add your 1-minute interval task logic here

def my_5_minute_job():
    # Helper.log_scraping_news('Test Portal')
    log_cron_run('5-Minute Job')
    # Add your 5-minute interval task logic here

def my_hourly_job():
    log_cron_run('Hourly Job')
    # Add your hourly task logic here

def my_daily_job():
    log_cron_run('Daily Job')
    # Add your daily task logic here


def cron_scrape_all_jugantor_news():
    Scraping.scrape_all_jugantor_news()

def cron_scrape_all_bd_pratidin_news():
    Scraping.scrape_all_bd_pratidin_news()

def cron_scrape_all_bbc_bangla_news():
    Scraping.scrape_all_bbc_bangla_news()

def cron_scrape_all_daily_star_news():
    Scraping.scrape_all_daily_star_news()

def cron_post_Gemten_News_page():
    Helper.post_Gemten_News_page()


if __name__ == '__main__':
    print("Starting scheduled cron jobs...\n")
    my_scheduled_job()
    my_1_minute_job()
    my_5_minute_job()
    my_hourly_job()
    my_daily_job()
    print("\nAll scheduled cron jobs completed.")


