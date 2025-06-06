import os
from News.models import Template
from django.core.files import File
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Upload template images from local folder'

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str, help='Folder path to upload images from')

    def handle(self, *args, **kwargs):
        folder = kwargs['folder']
        if not os.path.isdir(folder):
            self.stdout.write(self.style.ERROR(f"Folder {folder} does not exist"))
            return
        
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                filepath = os.path.join(folder, filename)
                with open(filepath, 'rb') as f:
                    django_file = File(f)
                    # Use filename without extension as name or customize as you want
                    name = os.path.splitext(filename)[0]
                    template = Template(name=name)
                    template.image.save(filename, django_file, save=True)
                    self.stdout.write(self.style.SUCCESS(f'Uploaded {filename}'))

