from .base import *

# Quick-start development settings - unsuitable for production
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = os.environ.get("SECRET_KEY") or "DEVELOPMENT!!"
DEBUG = bool(strtobool(os.environ.get("DEBUG") or "True"))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
#
# Comment out STORAGES["staticfiles"]["BACKEND"] and uncomment DEBUG = False to
# test with production static files.

# DEBUG = False
STORAGES["staticfiles"][
    "BACKEND"
] = "django.contrib.staticfiles.storage.StaticFilesStorage"


# Django Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
)
