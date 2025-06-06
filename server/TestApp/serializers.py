from rest_framework import serializers
from .models import TestImage


class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = '__all__'
        read_only_fields = ['is_edited', 'edited_image', 'all_edited_image']
