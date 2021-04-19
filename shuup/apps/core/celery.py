"""
Celery task queue
"""

import os
import logging.config

from celery import Celery
from django.conf import settings
from celery.signals import setup_logging
import dotenv


dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shuup.settings")


@setup_logging.connect
def configure_logging(*args, **kwags):
    logging.config.dictConfig(settings.LOGGING)


celery_app = Celery(settings.APPLICATION_NAME)
celery_app.config_from_object("django.conf:settings")
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
celery_app.CELERY_BROKER_URL = settings.CELERY_BROKER_URL
celery_app.CELERY_RESULT_BACKEND = settings.CELERY_RESULT_BACKEND
celery_app.conf.CELERY_TASK_ALWAYS_EAGER = settings.CELERY_TASK_ALWAYS_EAGER
celery_app.conf.CELERY_ACCEPT_CONTENT = ["application/json"]
celery_app.conf.CELERY_TASK_SERIALIZER = "json"
celery_app.conf.CELERY_RESULT_SERIALIZER = "json"
celery_app.conf.CELERY_TIMEZONE = "UTC"
celery_app.conf.CELERY_ROUTES = {}
celery_app.conf.CELERYBEAT_SCHEDULE = {}
