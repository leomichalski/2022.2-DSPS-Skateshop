from store.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q=137gn%uu)+zdjc_k(m*6la$@)2plx=@(c-)u)i^0o+7o4s^l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.15.16"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DEBUG_PROPAGATE_EXCEPTIONS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = BASE_DIR / 'static'
STATIC_ROOT = BASE_DIR / 'static'

# Media

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'




