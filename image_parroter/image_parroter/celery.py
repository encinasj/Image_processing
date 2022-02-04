import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGs_MODULE', 'image_parroter.settings')


celery_app = Celery('image_parroter')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

