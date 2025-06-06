from .views import TestApiView, TestImageProcessingApiView
from django.urls import path

urlpatterns = [
    path('test/', TestApiView.as_view(), name='test'),
    path('test/image-processing/', TestImageProcessingApiView.as_view(), name='test image processing'),
]