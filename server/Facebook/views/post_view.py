import json, os
from PIL import Image
from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Helper import constants
from datetime import datetime
from Helper.helpers import Helper
from News.models import News, Template
from ..facebook_helper import Facebook
from Helper.response import ResponseHelper
from TestApp.Test_News_Templates import helper_image


class PostToFacebookPage(APIView):
    def get(self, request):
        response = {
            'status': True,
            'message': 'Success! Facebook Post API via Docker working correctly!'
        }

        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request):
        print('\n' + '&&&'*30)
        news = News.objects.get(id=request.data['id'])
        stored_pages = []
        if request.data.get('storedPages'):
            stored_pages = json.loads(request.data.get('storedPages'))
        template = Template.objects.get(id=request.data['template_id'])
        
        template_code = f'template{template.id}'
        if template_code not in news.all_edited_image:
            self.process_news_with_new_template(news, template, template_code)

        success_post_count, failed_post_count = 0, 0
        image_path = os.path.join(settings.MEDIA_ROOT, news.all_edited_image.get(template_code))
        for page in stored_pages:
            # categories = page['categories']
            # if news.category not in categories:
            #     print('This page does not have', news.category, 'category')
            #     print('Skipping this page')
            #     continue

            page_id, access_token = page['pageId'], page['accessToken']
            timestamp = timezone.localtime().strftime("%d %B, %Y - %I:%M:%S %p")
            print('*****', str(timestamp), 'Start Posting on', page_id)
            
            intro = news.intro or news.title or 'তার সঙ্গে কাজ করা আমা'
            caption=f'{intro} \n\nMore details in Comment Section. {constants.POST_HASHTAGS}'
            
            # continue
            fb = Facebook(page_id=page_id, page_access_token=access_token)
            response = fb.post_local_image_to_page(image_path=image_path, caption=caption)
            if response.status_code == 200:
                success_post_count += 1
                full_comments = f'{news.intro}'
                if full_comments:
                    full_comments += '\n\n'
                full_comments += f'More details: {news.url} {constants.POST_HASHTAGS}'
                # print('full_comments:', full_comments)
                fb.comment_on_post(response.json().get('post_id'), comment=full_comments)
            else:
                failed_post_count += 1
            
            timestamp = timezone.localtime().strftime("%d %B, %Y - %I:%M:%S %p")
            print('*****', str(timestamp), 'End Posting on', page_id)
        
        response = ResponseHelper.get_post_to_facebook_response(success_post_count, failed_post_count)
        return Response(response, status=status.HTTP_200_OK)

    def process_news_with_new_template(self, news, template, template_code):
        file_name = os.path.splitext(os.path.basename(news.image.name))[0]
        edited_name = f"{file_name}_template{template.id}.jpg"
        edited_path = os.path.join(settings.MEDIA_ROOT, 'edited_images', edited_name)
        os.makedirs(os.path.dirname(edited_path), exist_ok=True)


        # === Load and process image ===
        news_image = Image.open(news.image.path).convert("RGBA")
        template_image = Image.open(template.image.path).convert("RGBA")
        # image = Helper.processing_background_image_and_template_image(news_image, template_image, news.title, is_bangla_news=news.type=='bn')
        image = Helper.processing_background_image_and_new_template_image(news_image, template_image, news.title, news.source, news.type=='bn')
        if image.mode == "RGBA":
            image = image.convert("RGB")
        image.save(edited_path) # Save processed image
        
        # Store path in all_edited_image
        news.is_edited = True
        news.all_edited_image[template_code] = f"edited_images/{edited_name}"
        news.save()
        return news


class PostToGemtenFacebookPage(APIView):
    def get(self, request):
        added = [4810, 4811, 4812]
        from Helper import constants
        from django.core.cache import cache
        cache.set(constants.GEMTEN_TERABYTE_PAGE_ID, added, timeout=None)

        title = "More Details in Comment Section."

        full_comments = f"{title} {constants.POST_HASHTAGS}"
        print(full_comments)
        response = {
            'status': True,
            'message': 'Success! Facebook Post API via Docker working correctly!'
        }

        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        response = {
            'status': True,
            'message': 'Success! Facebook Post API via Docker working correctly!'
        }

        print('\n' + '&*&'*30)
        ids = request.data['ids']
        print('^^ &^', ids)
        for _ in range(10):
            for id in ids:
                print(id, end=' ')
                template_id = Helper.get_page_template_id(id)
                print(template_id)

        return Response(response, status=status.HTTP_200_OK)

# https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Faccounts%3Faccess_token%3DLONG_LIVED_USER_TOKEN&version=v22.0