from .base import *
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "testuser",
        "PASSWORD": "testpass",
        "HOST": "localhost",
        "PORT": "5434",
    }
}
