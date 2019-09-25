# Requirements
- `Python >= 3.7`
- `pip`
- `Postgresql >= 11`
- `OpenLDAP`

## Deployment
- `Apache2`
- `mod_wsgi`

# Setup
## Set up Python environment
`pip install -r requirements/production.txt`

## Set local settings
Put custom settings in `config/settings/local_settings.py`

For Django related variables see [Django's documentation](https://docs.djangoproject.com/en/dev/ref/settings/).
- `DJANGO_SECRET_KEY`
- `DATABASE_URL`
- `DJANGO_ALLOWED_HOSTS` (List)

### LDAP
See [django-auth-ldap docs](https://django-auth-ldap.readthedocs.io/en/latest/authentication.html#server-config).
- `LDAP_SERVER_URI`
- `LDAP_USER_DN`
- `LDAP_USER_PASSWORD`

## Run database migrations
- `python manage.py migrate --no-input`. See [Django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate).

## Update translation fields
- `python manage.py update_translation_fields`. See [wagtail-modeltranslation docs](https://wagtail-modeltranslation.readthedocs.io/en/latest/management%20commands.html#the-update-translation-fields-command).

## Update search index
- `python manage.py update_index`. See [Wagtail docs](https://docs.wagtail.io/en/latest/reference/management_commands.html#update-index)

## Compile translation
- `python manage.py compilemessages`. See [Django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-compilemessages)

## Collect static files
- `python manage.py collectstatic`. See [Django docs](https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#collectstatic)

# Deployment with Apache and mod_wsgi
See [Django docs](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/).