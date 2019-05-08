# Setup

## Set environmental variables
See [Django's documentation](https://docs.djangoproject.com/en/dev/ref/settings/).
- `DJANGO_SECRET_KEY`
- `DATABASE_URL`
- `DJANGO_ADMIN_URL`

### LDAP
- `LDAP_SERVER_URI`

## Run Migrations
- `python manage.py migrate --no-input`. See [Django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate).
- `python manage.py update_translation_fields`. See [wagtail-modeltranslation docs](https://wagtail-modeltranslation.readthedocs.io/en/latest/management%20commands.html#the-update-translation-fields-command).