# Setup

## Requirements
- `Python >= 3.7`
- `pip`
- `Postgresql >= 11`
- `OpenLDAP`

## Set up Python environment
`pip install -r requirements/production.txt`

## Set environmental variables
For Django related variables see [Django's documentation](https://docs.djangoproject.com/en/dev/ref/settings/).
- `DJANGO_SECRET_KEY`
- `DATABASE_URL`
- `DJANGO_ALLOWED_HOSTS` (List)
- `DJANGO_ADMIN_URL`

### LDAP
- `LDAP_SERVER_URI`

## Run Migrations
- `python manage.py migrate --no-input`. See [Django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate).
- `python manage.py update_translation_fields`. See [wagtail-modeltranslation docs](https://wagtail-modeltranslation.readthedocs.io/en/latest/management%20commands.html#the-update-translation-fields-command).