# Development Notes

## Translation
In `urls.py`, `i18n_patterns()` can be passed `prefix_default_language=False`. This disables the language url prefix for the default language, but results in breaking Django's `set_language` view (used by language selection dropdown), as it is not able to get the current url without language prefix. This could be solved by passing the redirect location as POST parameter `next`, and would require to write a hacky solution to remove the language prefix, if it exists.

Individual StreamField blocks are not translateable yet, see [this issue](https://github.com/infoportugal/wagtail-modeltranslation/issues/82).

Empty fields (excluding StreamFields) are automatically populated with the the default langugage content due to [this issue](https://github.com/infoportugal/wagtail-modeltranslation/issues/247).

## Imports
Django lets you import `<app_label>`, which will result in errors later. Only import `mpicms.<app_label>`, as specified in the app configs.

## Migrations
Due to an [issue](https://github.com/infoportugal/wagtail-modeltranslation/issues/240) with wagtail-modeltranslation when using a custom user model, `makemigrations` has to run twice, first without wagtail-modelmigrations and the second time, with it. For details see the issue.

## Search Index
After objects have been created through a script, `manage.py update_index` sould be run. See [Wagtail docs](https://docs.wagtail.io/en/latest/topics/search/indexing.html#the-update-index-command).