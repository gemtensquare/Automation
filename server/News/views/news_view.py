import os
from datetime import datetime
from rest_framework import status
from django.utils import timezone
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models import *
from ..serializers import *
from Helper import constants
from Helper.scraping import Scraping
from Helper.response import ResponseHelper


class NewsAPIView(APIView):
    def get(self, request):
        print()
        print(')(' * 30)
        # self.redis_test_view()
        # news_ids = cache.get('571480596045760', [])
        # news_ids += [1,3,4,5,2]
        # cache.set('571480596045760', news_ids)
        # cache.delete('571480596045760')
        print("GEMTEN_NEWS Stored News Ids:", cache.get(constants.GEMTEN_NEWS_PAGE_ID, []))
        print("GEMTEN_SPORTS Stored News Ids:", cache.get(constants.GEMTEN_SPORTS_PAGE_ID, []))
        print("GEMTEN_ShowBiz Stored News Ids:", cache.get(constants.GEMTEN_ShowBiz_PAGE_ID, []))
        print("GEMTEN_CRICKET Stored News Ids:", cache.get(constants.GEMTEN_CRICKET_PAGE_ID, []))
        print("GEMTEN_FOOTBALL Stored News Ids:", cache.get(constants.GEMTEN_FOOTBALL_PAGE_ID, []))
        print("GEMTEN_TERABYTE Stored News Ids:", cache.get(constants.GEMTEN_TERABYTE_PAGE_ID, []))

        start_time = timezone.localtime()
        
        news = News.objects.all()

        response = ResponseHelper.get_news_response(NewsSerializer(news, many=True))
        
        end_time = timezone.localtime()
        duration = end_time - start_time
        response['response_duration'] = duration.total_seconds()
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request):
        start_time = timezone.localtime()
        print('$$$$'*20)
        print(request.data)
        categories = request.data.get('categories', None)
        print(categories)
        if not categories:
            return self.get(request)
        
        if 'Technology' in categories or 'Science' in categories:
            categories.append('TechStartup')

        news = News.objects.filter(category__in=categories)
        response = ResponseHelper.get_news_response(NewsSerializer(news, many=True))
        
        end_time = timezone.localtime()
        duration = end_time - start_time
        response['response_duration'] = duration.total_seconds()
        return Response(response, status=status.HTTP_200_OK)

    def redis_test_view(self):
        cache.set('test', 'test')
        cache.set('arr', [1, 2, 4, 4, 5, 5])
        # cache.delete('571480596045760') 
        print("Stored News Ids:", cache.get('571480596045760', []))

        new_arr = cache.get('arr')
        if not new_arr:
            new_arr = []

        new_arr += [5,5,4,3,5,6,4,6,3,5,6,6,3]
        cache.set('arr', new_arr)

        
        print(cache.get('test'))
        print(cache.get('arr'))
        print(')(' * 20)
        
        

class RemoveAllNews(APIView):
    def get(self, request):
        News.objects.all().delete()
        response = {
            'status': True,
            'message': 'All news deleted successfully!'
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
class ScrapeAllNews(APIView):
    def get(self, request):
        print('\n', ')(' * 30)
        print('Scraping all news...')
        start_time = datetime.now()
        data = Scraping.scrape_all_news()
        response = ResponseHelper.get_new_news_added_response(data)
        end_time = datetime.now()
        duration = end_time - start_time
        response['response_duration'] = duration.total_seconds()
        return Response(response, status=status.HTTP_200_OK)
    
    
class ClearRedisCache(APIView):
    def get(self, request):
        from django.core.cache import cache
        Gemten_Sports = cache.get(constants.GEMTEN_SPORTS_PAGE_ID, [])
        cache.clear()
        cache.set(constants.GEMTEN_SPORTS_PAGE_ID, Gemten_Sports)
        response = {
            'status': True,
            'message': 'Redis cache cleared successfully!'
        }
        return Response(response, status=status.HTTP_200_OK)


class GetRedisCache(APIView):
    def get(self, request):
        # cache.set(constants.GEMTEN_NEWS_PAGE_ID, [1, 2, 3])
        response = {
            'status': True,
            'message': "Got latest news queue from Redis!",
            'data': {
                f'Gemten News': cache.get(constants.GEMTEN_NEWS_PAGE_ID, []),
                f'Gemten ShowBiz': cache.get(constants.GEMTEN_ShowBiz_PAGE_ID, []),
                f'Gemten Terabyte': cache.get(constants.GEMTEN_TERABYTE_PAGE_ID, []),
            }
        }
        return Response(response, status=status.HTTP_200_OK)

class TemplateApiView(APIView):
    def get(self, request):
        template = Template.objects.all()
        response = {
            'status': True,
            'message': 'Success! Template API via Docker working correctly!',
            'data': TemplateSerializer(template, many=True).data
        }
        return Response(response, status=status.HTTP_200_OK)