
CRONJOBS = [
    # ('*/5 * * * *', 'Helper.cron.my_5_minute_job'),
    ('*/5 * * * *', 'Helper.cron.cron_post_Gemten_News_page'),
    ('*/10 * * * *', 'Helper.cron.cron_scrape_all_jugantor_news'),
    ('*/15 * * * *', 'Helper.cron.cron_scrape_all_bbc_bangla_news'),
    ('*/15 * * * *', 'Helper.cron.cron_scrape_all_bd_pratidin_news'),
    ('*/20 * * * *', 'Helper.cron.cron_scrape_all_daily_star_news'),
    # ('*/1 * * * *', 'Helper.cron.my_1_minute_job'),
    # ('0 * * * *', 'Helper.cron.my_hourly_job'),
    # ('0 0 * * *', 'Helper.cron.my_daily_job'),
]