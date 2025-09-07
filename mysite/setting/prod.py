from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@e!15wuv6ph(tuyjo-!_9p=ox01kw*8k)**cxcq-fok&e#etdj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}





STATICFILES_DIRS = [
    BASE_DIR / "mysite" / "static",
]


STATIC_ROOT = BASE_DIR / "staticfiles"  # پوشه خروجی collectstatic

MEDIA_ROOT = BASE_DIR / 'media'



csrf_cookie_secret = True