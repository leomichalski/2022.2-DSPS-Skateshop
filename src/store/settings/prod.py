import environ

from store.settings.base import *

env = environ.Env()

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "www.dspsskateshop.com.br",
    "dspsskateshop.com.br"
]

INSTALLED_APPS.append(
    "storages",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DATABASE_NAME"),
        'HOST': env("DATABASE_HOST"),
        'USER': env("DATABASE_USERNAME"),
        'PASSWORD': env("DATABASE_PASSWORD")
    }
}

# aws s3 settings
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # not a secret
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')  # not a secret
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=172800'}

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'store.storage.StaticStorage'
# s3 media settings
MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'store.storage.MediaStorage'
