from rest_framework import serializers
from ..models import News
from django.conf import settings

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'