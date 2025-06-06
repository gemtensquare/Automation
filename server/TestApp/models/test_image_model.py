from django.db import models

class TestImage(models.Model):
    image = models.ImageField(upload_to='test_images/')

    is_edited = models.BooleanField(default=False)
    edited_image = models.ImageField(upload_to='edited_images', null=True, blank=True)
    all_edited_image = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.image
    
