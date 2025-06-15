from django.db import models

class Template(models.Model):
    page_name = models.CharField(max_length=100)
    page_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='template_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.page_name} (id: {self.id})"
