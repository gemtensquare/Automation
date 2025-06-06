from django.db import models


class News(models.Model):
    intro = models.TextField()
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=1000)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    source = models.CharField(max_length=50)

    image = models.ImageField(upload_to='news_images')
    type = models.CharField(max_length=10, default='en')
    category = models.CharField(max_length=50, null=True, blank=True)

    is_edited = models.BooleanField(default=False)
    all_edited_image = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']