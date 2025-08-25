from .base import *
DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prod_db",
        "USER": "produser",
        "PASSWORD": "prodpass",
        "HOST": "localhost",
        "PORT": "5435",
    }
}
