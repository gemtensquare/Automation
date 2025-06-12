from .views import *
from django.urls import path

from .tests import *

urlpatterns = [
    path('genarate/', TestImage.as_view(), name='genarate test image'),
    path('post/to/facebook/', PostToFacebookPage.as_view(), name='post to facebook'),
    path('post/to/gemten/facebook/', PostToGemtenFacebookPage.as_view(), name='post to gemten facebook'),
]