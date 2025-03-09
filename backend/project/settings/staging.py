from .base import *

DEBUG = False
ALLOWED_HOSTS = ["staging.myapp.com"]

# Logging for staging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "/var/log/django-staging.log",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "ERROR",
    },
}
