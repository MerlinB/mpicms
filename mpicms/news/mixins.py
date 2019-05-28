from django.apps import apps
from django.db import models


class NewsMixin(models.Model):

    @property
    def news(self):
        news_page = apps.get_model('news', 'NewsPage')
        return self.get_children().type(news_page)

    class Meta:  # noqa
        abstract = True
