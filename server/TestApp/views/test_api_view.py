from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import TestImageSerializer
from ..models import TestImage

from Helper.helpers import Helper
from Helper.scraping import Scraping
from Helper.response import ResponseHelper

class TestApiView(APIView):
    def get(self, request):
        data = []

        data += Scraping.scrape_all_jugantor_news()
        # data += Scraping.scrape_all_bbc_bangla_news()
        # data += Scraping.scrape_all_daily_star_news()
        # data += Scraping.scrape_all_bd_pratidin_news()
        
        response = ResponseHelper.get_new_news_added_response(data)
        return Response(response, status=status.HTTP_200_OK)
    


# class TestImageProcessingApiView(APIView):
#     def get(self, request):
#         all_Img = TestImage.objects.all()
#         for img in all_Img:
#             print(img.id, img.image.url)
#         response = {
#             'status': True,
#             'message': 'Success. Test Image Processing Api via Docker working correctly! Accah? Haha!'
#         }
#         return Response(response, status=status.HTTP_200_OK)



import os
from PIL import Image, ImageDraw, ImageFont
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings


class TestImageProcessingApiView(APIView):
    def get(self, request):
        all_imgs = TestImage.objects.all()

        for img in all_imgs:
            original_path = img.image.path  # Full path to original image
            file_name = os.path.basename(original_path)
            edited_name = f"edited_{file_name}"
            edited_path = os.path.join(settings.MEDIA_ROOT, 'edited_images', edited_name)

            # Ensure the directory exists
            os.makedirs(os.path.dirname(edited_path), exist_ok=True)

            # === Load and process image ===
            image = Image.open(original_path).convert("RGB")
            image = self.helper_image(image)

            # Save processed image
            image.save(edited_path)

            # Save path in model
            img.edited_image.name = f"edited_images/{edited_name}"
            img.is_edited = True

            # Add to all_edited_image list
            if not isinstance(img.all_edited_image, list):
                img.all_edited_image = []
            img.all_edited_image.append(f'/Media/{img.edited_image.name}')

            img.save()

        data = TestImageSerializer(TestImage.objects.all(), many=True).data

        return Response({
            'status': True,
            'message': 'All images processed and saved successfully.',
            'data': data
        }, status=status.HTTP_200_OK)
    
    def helper_image(self, image):
        image = image.resize((800, 450))  # 16:9 ratio

        draw = ImageDraw.Draw(image)

        # Load fonts
        try:
            font_headline = ImageFont.truetype("arialbd.ttf", 40)
            font_subheadline = ImageFont.truetype("arialbd.ttf", 25)
            font_small = ImageFont.truetype("arial.ttf", 20)
        except:
            font_headline = ImageFont.load_default()
            font_subheadline = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # === TOP Banner (BREAKING NEWS) ===
        draw.rectangle([(0, 0), (image.width, 60)], fill="red")
        draw.text((10, 10), "BREAKING NEWS", font=font_headline, fill="white")

        # === Main Headline ===
        draw.rectangle([(0, 70), (image.width, 140)], fill=(0, 0, 0, 180))
        draw.text((20, 80), "Unexpected Weather Hits the City!", font=font_headline, fill="white")

        # === Subheadline ===
        draw.text((20, 150), "Heavy rain floods major roads this morning.", font=font_subheadline, fill="white")

        # === Reporter Info and Location ===
        draw.text((20, 190), "Reported by: Md. Sishir Rahman Siam (@shishirRsiam)", font=font_small, fill="white")
        draw.text((20, 220), "Lalmonirhat - 8:30 AM", font=font_small, fill="white")

        # === Bottom Ticker ===
        ticker_height = 50
        draw.rectangle([(0, image.height - ticker_height), (image.width, image.height)], fill="black")
        draw.text((10, image.height - ticker_height + 15), "Stay tuned for more updates...", font=font_small, fill="yellow")

        # Show and Save
        return image
        # image.save("news_template_full.jpg")

