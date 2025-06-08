import json, os
from PIL import Image
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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
            categories = page['categories']
            # if news.category not in categories:
            #     print('This page does not have', news.category, 'category')
            #     print('Skipping this page')
            #     continue

            page_id, access_token = page['pageId'], page['accessToken']
            
            print('*****', str(datetime.now()), 'Start Posting on', page_id)
            fb = Facebook(page_id=page_id, page_access_token=access_token)
            response = fb.post_local_image_to_page(image_path=image_path, caption=f'{news.title}. More details in Comment Section.')
            if response.status_code == 200:
                success_post_count += 1
                fb.comment_on_post(response.json().get('post_id'), comment=f'More details: {news.url}')
            else:
                failed_post_count += 1
            print('*****', str(datetime.now()), 'End Posting on', page_id)
        
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


# https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Faccounts%3Faccess_token%3DLONG_LIVED_USER_TOKEN&version=v22.0