from .base import *
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
