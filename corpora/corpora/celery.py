# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from corpus.tasks_scheduled import CELERYBEAT_SCHEDULE as corpus_schedule
from people.tasks_scheduled import CELERYBEAT_SCHEDULE as people_schedule


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corpora.settings')

app = Celery('corpora')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


CELERYBEAT_SCHEDULE = corpus_schedule
CELERYBEAT_SCHEDULE.update(people_schedule)

app.conf.beat_schedule = CELERYBEAT_SCHEDULE
