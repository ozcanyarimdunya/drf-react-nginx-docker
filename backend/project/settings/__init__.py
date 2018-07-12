from .base import *

INSTALLED_APPS += [
    'rest_framework',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ALLOWED_HOSTS += ['*']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/assets/dev-static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'project/assets/static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "project/assets/media")

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'pass123',
    'HOST': 'db',  # set in docker-compose.yml
    'PORT': 5432  # default postgres port
}
