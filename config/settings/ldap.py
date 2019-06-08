import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

from .base import *  # noqa
from .base import env


# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]

AUTH_LDAP_SERVER_URI = env('LDAP_URI')

LDAP_USER_NAMES = env('LDAP_USER_NAMES', default="dc=user,dc=apps,dc=molgen,dc=mpg,dc=DE")

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER
}

AUTH_LDAP_BIND_DN = env('LDAP_USER_DN', default="cn=mpicms,dc=ldap,dc=apps,dc=molgen,dc=mpg,dc=DE")
AUTH_LDAP_BIND_PASSWORD = env('LDAP_USER_PASSWORD')
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