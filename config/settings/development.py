from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Override DB to SQLite for quick local dev (comment out to use .env PostgreSQL)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
