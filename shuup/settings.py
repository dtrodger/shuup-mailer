"""
Django settings
"""

import os

from shuup import utils


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = utils.get_env_var("SHUUP_SECRET")
DEBUG = utils.get_env_var("SHUUP_DEBUG", is_bool=True)
TEMPLATE_DEBUG = utils.get_env_var("SHUUP_TEMPLATE_DEBUG", is_bool=True)
ALLOWED_HOSTS = utils.get_env_var("SHUUP_ALLOWED_HOSTS", is_list=True)
INTERNAL_IPS = utils.get_env_var("SHUUP_INTERNAL_IPS", is_list=True)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shuup.apps.core',
    'shuup.apps.mailer',
)
MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
ROOT_URLCONF = 'shuup.urls'
WSGI_APPLICATION = 'shuup.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': utils.get_env_var("SHUUP_DB_ENGINE"),
        'NAME': utils.get_env_var("SHUUP_DB_NAME"),
    }
}
STATIC_URL = '/static/'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
APPLICATION_NAME = utils.get_env_var("SHUUP_APPLICATION_NAME")
CELERY_BROKER_URL = utils.get_env_var("SHUUP_CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = utils.get_env_var("SHUUP_CELERY_RESULT_BACKEND")
CELERY_TASK_ALWAYS_EAGER = utils.get_env_var("SHUUP_CELERY_TASK_ALWAYS_EAGER", is_bool=True)
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "shuup", "apps", "core", "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
        },
    },
]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "stdout": {"class": "logging.StreamHandler", "formatter": "standard"},
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": "logs/shuup.log",
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10,
        }
    },
    "loggers": {
        "": {
            "handlers": ["stdout", "file"],
            "level": utils.get_env_var("SHUUP_LOG_LEVEL"),
        },
    },
}
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache",
    }
}