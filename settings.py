import os
from pathlib import Path
from decouple import config
import dj_database_url
from django.core.exceptions import ImproperlyConfigured
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-y0&g8dvlox@d92kfqfl+y%ad2ct)go+*+$)a7h7c+gsqpq@^bf')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)  # Set default to False for safety

ALLOWED_HOSTS = []
if not DEBUG:
    # Production-specific settings
    ALLOWED_HOSTS = [config('ALLOWED_HOST', default='your_production_hostname.com')]  # Replace with your actual hostname
    if 'RAILWAY_ENVIRONMENT' in os.environ:
        # Running on Railway, trust the X-Forwarded-Proto header
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        USE_X_FORWARDED_HOST = True
        SECURE_SSL_REDIRECT = True  # Force HTTPS
        SESSION_COOKIE_SECURE = True  # HTTPS-only cookies
        CSRF_COOKIE_SECURE = True  # HTTPS-only CSRF token
        logger.info("Running in Railway environment, security settings enabled.")
    else:
        logger.warning("Running in production, but not in Railway. Please ensure security settings are configured manually.")
else:
    # Development-specific settings
    ALLOWED_HOSTS = ['*']  # Allow all hosts in development
    logger.info("Running in development mode. ALLOWED_HOSTS set to '*', security settings relaxed.")

# Application definition
INSTALLED_APPS = [
    'channels',
    'rest_framework',
    'embed_video',
    "query_search",
    "messaging",
    "ml",
    "social_app",
    "xvoice",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myvoice.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Templates outside apps
        'APP_DIRS': True,  # Allow Django to search app-specific templates
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myvoice.wsgi.application"

# Database configuration
DATABASES = {
    'default': dj_database_url.parse(config('postgresql://postgres:OjCvFOhChzaPhZzgyJuQEKtwNFudhZyB@postgres.railway.internal:5432/railway', default='sqlite:///db.sqlite3')) # or whatever is appropriate for dev
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL to access static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Place custom static files here
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
ASGI_APPLICATION = 'myvoice.asgi.application'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('REDIS_URL', default='redis://127.0.0.1:6379/1'),  #Use decouple
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_DOMAIN = None # should be .domain.com for it to work on domain.com, and all subdomain.domain.com; also useful for local testing
SESSION_COOKIE_SECURE = not DEBUG #  only in production, session_cookie_secure should be True

# Django CORS settings.  These should be environment variables in production.
CORS_ORIGIN_WHITELIST = [config('CORS_ORIGIN', default='http://localhost:3000')], # and/or whatever your development port is.  Should be an environment variable.
CORS_ALLOW_CREDENTIALS = True

SESSION_REDIS = {
    'host': config('REDIS_HOST', default='127.0.0.1'),  # Use decouple for Redis settings
    'port': config('REDIS_PORT', cast=int, default=6379), #Use decouple
    'db': config('REDIS_DB', cast=int, default=1),   #Use decouple
    'password':config('None, default=') ,  # Set password to None if no password is used
    'prefix': 'session',
    'socket_timeout': 1,
    'retry_on_timeout': False
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when_cross-origin'
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = [config('CSRF_ORIGIN', default='http://localhost:8000')] # in prod
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
