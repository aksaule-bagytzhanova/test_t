PROJECT_APPS = (
    'api',
)

THIRD_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg'
)


DEFAULT_APPS = (
                   'django.contrib.admin',
                   'django.contrib.auth',
                   'django.contrib.contenttypes',
                   'django.contrib.sessions',
                   'django.contrib.messages',
                   'django.contrib.staticfiles',
               ) + THIRD_APPS + PROJECT_APPS
