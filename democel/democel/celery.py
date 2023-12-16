import os  
  
from celery import Celery  
from celery.schedules import crontab  
  
# Set the default Django settings module for the 'celery' program.  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'democel.settings')  
  
#pass the project name in Celery(project_name)  
app = Celery('democel')  
  
# Using a string here means the worker doesn't have to serialize  
# the configuration object to child processes.  
# - namespace='CELERY' means all celery-related configuration keys  
#   should have a `CELERY_` prefix.  
app.config_from_object('django.conf:settings', namespace='CELERY')  
  
#Celery Beat Settings  
app.conf.beat_schedule = {  
    'send-mail-every-day-at-8' :  {  
        'task': 'emailExample.tasks.send_mail_func',  
        'schedule': crontab(hour = 15, minute = 42),  
  
    }  
      
}  
  
# Load task modules from all registered Django apps.  
app.autodiscover_tasks()  
  
@app.task(bind=True)  
def debug_task(self):  
    print(f'Request: {self.request!r}')