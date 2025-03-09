import os

ENVIRONMENT = os.getenv("DJANGO_ENV", "development")

if ENVIRONMENT == "development":
    from .development import *
elif ENVIRONMENT == "staging":
    from .staging import *
elif ENVIRONMENT == "production":
    from .production import *
