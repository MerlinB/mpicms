from .base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = 'XBlibrFtVb24Dig6CCMAw7Kv3FpXpJYmEZMdpRlnRdTzQpNdTPZ1TtvqKiQu9caf'

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += [  # noqa F405
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'console': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

try:
    from local_settings import *  # noqa
except ImportError:
    pass
