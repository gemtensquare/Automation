from News.models import News




News.objects.filter(type='bn').delete()

print('Delete Done')