from .base import *
DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com"]

DATABASES = {
    "default": dj_database_url.config(
        default=env(
            "DATABASE_URL",
            default="postgresql://myuser:mypassword@db:5432/mydb",
        ),
        conn_max_age=600,
        ssl_require=env.bool("DB_SSL_REQUIRED", default=False),
    )
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/1",  # service name = redis
    }
}

CELERY_BROKER_URL = 'amqp://user:pass@rabbitmq:5672//'
CELERY_RESULT_BACKEND = "rpc://"