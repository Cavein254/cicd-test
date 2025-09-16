from .base import *

from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dev_db",
        "USER": "devuser",
        "PASSWORD": "devpass",
        "HOST": "localhost",
        "PORT": "5433",
    }
}



CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/1",  # service name = redis
    }
}

CELERY_BROKER_URL = 'amqp://user:pass@rabbitmq:5672//'
CELERY_RESULT_BACKEND = "rpc://"