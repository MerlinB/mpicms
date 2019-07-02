import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

from .base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = None
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['intranet.molgen.mpg.de']

# DATABASES
# ------------------------------------------------------------------------------
DATABASES['default']['CONN_MAX_AGE'] = 60  # noqa F405

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]

# AUTHENTICATION
WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = False
WAGTAIL_PASSWORD_RESET_ENABLED = False
WAGTAILUSERS_PASSWORD_ENABLED = False

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]

AUTH_LDAP_SERVER_URI = 'ldaps://ldap.molgen.mpg.de/'

LDAP_USER_NAMES = "dc=user,dc=apps,dc=molgen,dc=mpg,dc=DE"

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER
}

AUTH_LDAP_BIND_DN = "cn=mpicms,dc=ldap,dc=apps,dc=molgen,dc=mpg,dc=DE"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
        LDAP_USER_NAMES,
        ldap.SCOPE_SUBTREE,
        "(uid=%(user)s)")


AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s," + LDAP_USER_NAMES

AUTH_LDAP_FIND_GROUP_PERMS = False
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'ou=groups,dc=example,dc=com',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfNames)',
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    # 'is_staff': 'cn=staff,ou=groups,dc=example,dc=com',
    # 'is_superuser': 'cn=superuser,ou=groups,dc=example,dc=com',
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = 'MPI <info@molgen.mpg.de>'

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = DEFAULT_FROM_EMAIL
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[MPI CMS]'

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
    }
}

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
