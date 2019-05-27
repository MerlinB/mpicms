from django.db import models
from django.utils.translation import gettext as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.models import ClusterableModel


@register_snippet
class Person(index.Indexed, ClusterableModel):
    """
    A Django model to store People objects.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI (e.g. /admin/snippets/base/people/)
    `People` uses the `ClusterableModel`, which allows the relationship with
    another model to be stored locally to the 'parent' model (e.g. a PageModel)
    until the parent is explicitly saved. This allows the editor to use the
    'Preview' button, to preview the content, without saving the relationships
    to the database.
    https://github.com/wagtail/django-modelcluster
    """
    first_name = models.CharField(_("first name"), max_length=254)
    last_name = models.CharField(_("last name"), max_length=254)
    email = models.EmailField(_("email"), blank=True)
    phone = models.IntegerField(_("phone number"), blank=True, null=True)
    room = models.CharField(_("room"), max_length=25, blank=True)

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('room'),
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:  # noqa
        verbose_name = 'Person'
        verbose_name_plural = 'People'
