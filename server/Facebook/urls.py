from .views import *
from django.urls import path

from .tests import *

urlpatterns = [
    path('post/to/facebook/', PostToFacebookPage.as_view(), name='post to facebook'),
    path('genarate/', TestImage.as_view(), name='genarate test image'),
]