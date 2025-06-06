from .views import *
from django.urls import path

urlpatterns = [
    path('news/', NewsAPIView.as_view(), name='news'),
    path('template/', TemplateApiView.as_view(), name='template'),
    path('news/clear/', RemoveAllNews.as_view(), name='remove all news'),
    path('news/scrape/', ScrapeAllNews.as_view(), name='scrape all news'),
    path('redis/clear/', ClearRedisCache.as_view(), name='remove all news'),
    path('redis/', GetRedisCache.as_view(), name='get redis cache'),
]