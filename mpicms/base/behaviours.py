from django.db import models

from wagtail.core.models import Page


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).get(depth=3)

    class Meta:
        abstract = True
