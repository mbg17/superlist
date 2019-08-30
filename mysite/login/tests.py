from django.test import TestCase
import  os
import sys

# Create your tests here.
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()
    from login import  models
    obj = [models.UserInfo(name=f'test{104+i}') for i in range(100)]
    models.UserInfo.objects.bulk_create(obj,10)