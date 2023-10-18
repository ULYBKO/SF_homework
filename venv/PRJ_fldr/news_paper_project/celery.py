import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_paper_project.settings')
 
app = Celery('news_paper_project')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8_00_am': {
        'task' : 'news.tasks.weekly_notifications',
        'schedule' : crontab(),
        'args': ()
    }

}