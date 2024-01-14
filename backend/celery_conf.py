"""
Celery configuration module for backend.
"""

import os
from celery import Celery, shared_task
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend', broker=settings.BROKER_URL)

# Configure Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Define Celery tasks


@shared_task(bind=True)
def debug_task(self):
    """Function To Debug Task"""
    print(f'Request: {self.request!r}')


@shared_task
def sample_task():
    """Function to run simple Task"""
    print("The sample task just ran.")
