import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSampleTask.settings')

# Create default Celery app
app = Celery('DjangoSampleTask')


# namespace='CELERY' means all celery-related configuration keys
# should be uppercased and have a `CELERY_` prefix in Django settings.
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.beat_schedule = {
    "every_day": {
        "task": "transactions.tasks.change_transaction_status",
        "schedule": crontab(minute=0, hour=0),
    },
}

# When we use the following in Django, it loads all the <appname>.tasks
# files and registers any tasks it finds in them. We can import the
# tasks files some other way if we prefer.
app.autodiscover_tasks()