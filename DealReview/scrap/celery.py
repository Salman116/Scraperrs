from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrappers.settings')

app = Celery('scrap')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
    
app.conf.beat_schedule = {
    #Scheduler Name
    'scrapper_runner_schedular': {
        # Task Name (Name Specified in Decorator)
        'task': 'scrapper_runner',  
        # Schedule      
        'schedule': 86400.0, #seconds
    },
} 