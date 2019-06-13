from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class ContactGroups(Orderable, models.Model):
    """
    This defines the relationship between the `Group` within the `Contact` model below.
    """
    contact = ParentalKey(
        'Contact', related_name=_('groups'), on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        'personal.Group',
        related_name='contacts',
        on_delete=models.CASCADE,
        verbose_name=_('groups')
    )

    panels = [
        SnippetChooserPanel('group'),
    ]


@register_snippet
class Contact(index.Indexed, ClusterableModel):
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
    name = models.CharField(_("name"), max_length=254)
    email = models.EmailField(_("email"), blank=True)
    phone = models.IntegerField(_("phone number"), blank=True, null=True)
    room = models.CharField(_("room"), max_length=25, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('room'),
        InlinePanel(
            'groups', label="Groups",
            panels=None),
    ]

    search_fields = [
        index.SearchField('name'),
        index.SearchField('email'),
        index.SearchField('phone'),
        index.SearchField('room'),
        # index.SearchField('groups'),
    ]

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


@register_snippet
class Group(index.Indexed, ClusterableModel):
    name = models.CharField(_("name"), max_length=254)

    panels = [
        FieldPanel('name'),
    ]

    search_fields = [
        index.SearchField('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
