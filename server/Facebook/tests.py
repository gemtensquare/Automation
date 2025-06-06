from django.test import TestCase

from PIL import Image, ImageDraw, ImageFont
import io
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Helper.tests import generate_image

class TestImage(APIView):
    def get(request):
        response = generate_image(request)
        print(response)
        return Response({'Status': 'Success', 'Data': response}, status=status.HTTP_200_OK)