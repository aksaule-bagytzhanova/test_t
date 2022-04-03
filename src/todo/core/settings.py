import os
from pathlib import Path
from environ import Env
from core.helpers.apps import DEFAULT_APPS
from core.helpers.middleware import DEFAULT_MIDDLEWARE
from core.helpers.templates import DEFAULT_TEMPLATES
from core.helpers.validators import DEFAULT_AUTH_PASSWORD_VALIDATORS


BASE_DIR = Path(__file__).resolve().parent.parent
env: Env = Env()
Env.read_env()


SECRET_KEY = env.str(var='SECRET_KEY')
DEBUG = env.bool(var='DEBUG')
AUTH_USER_MODEL = 'api.User'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = DEFAULT_APPS
MIDDLEWARE = DEFAULT_MIDDLEWARE
ROOT_URLCONF = 'core.urls'
TEMPLATES = DEFAULT_TEMPLATES
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {'default': env.db()}
AUTH_PASSWORD_VALIDATORS = DEFAULT_AUTH_PASSWORD_VALIDATORS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = env.str(var='TIME_ZONE')
USE_I18N = True
USE_TZ = True

# Static | Media
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]

}
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
