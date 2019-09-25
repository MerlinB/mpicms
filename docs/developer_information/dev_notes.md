# Development Notes

## LDAP population
To populate the database with an existing LDAP user, run `django_auth_ldap.backend.LDAPBackend.populate_user()`. See [django-auth-ldap docs](https://django-auth-ldap.readthedocs.io/en/latest/users.html#updating-users) for details.

## Python shell
Access with `python manage.py shell --settings=config.settings.production`.

## Search Index
After objects have been created through a script, `manage.py update_index` sould be run. See [Wagtail docs](https://docs.wagtail.io/en/latest/topics/search/indexing.html#the-update-index-command).

## Translation
In `urls.py`, `i18n_patterns()` can be passed `prefix_default_language=False`. This disables the language url prefix for the default language, but results in breaking Django's `set_language` view (used by language selection dropdown), as it is not able to get the current url without language prefix. This could be solved by passing the redirect location as POST parameter `next`, and would require to write a hacky solution to remove the language prefix, if it exists.

Individual StreamField blocks are not translateable yet, see [this issue](https://github.com/infoportugal/wagtail-modeltranslation/issues/82).

Empty fields (excluding StreamFields) are automatically populated with the the default langugage content due to [this issue](https://github.com/infoportugal/wagtail-modeltranslation/issues/247).

### Updating translations
Run `python manage.py makemessages --ignore=users` to generate an updated `.po` file in `locale/de/LC_MESSAGES`. After editing the file, run `python manage.py compilemessages` to compile the new translations. See [Django docs](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/) for details.

## Imports
Django lets you import `<app_label>`, which will result in errors later. Only import `mpicms.<app_label>`, as specified in the app configs.