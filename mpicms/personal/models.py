from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class FilterableParentalKey(ParentalKey):
    def get_related_field(self):
        return self.remote_field


class ContactGroups(Orderable, models.Model):
    """
    This defines the relationship between the `Group` within the `Contact` model below.
    """
    contact = FilterableParentalKey(
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


class ContactPositions(Orderable, models.Model):
    """
    This defines the relationship between the `Position` within the `Contact` model below.
    """
    contact = FilterableParentalKey(
        'Contact', related_name=_('positions'), on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        'personal.Position',
        related_name='contacts',
        on_delete=models.CASCADE,
        verbose_name=_('positions')
    )

    panels = [
        SnippetChooserPanel('position'),
    ]


class ContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def include_inactive(self):
        return super().get_queryset()


@register_snippet
class Position(models.Model):
    title = models.CharField(_("title"), max_length=50)

    panels = [
        FieldPanel('title')
    ]

    search_fields = [
        index.SearchField('title')
    ]

    def __str__(self):
        return self.title


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
    title = models.CharField(_("title"), max_length=5, blank=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    email = models.EmailField(_("email"), blank=True)
    phone = models.CharField(_("phone number"), blank=True, max_length=50)
    room = models.CharField(_("room"), max_length=25, blank=True)
    is_active = models.BooleanField(_("is active"), default=True)
    priority = models.PositiveSmallIntegerField(
        _("priority"), blank=True, default=0, validators=[MaxValueValidator(999)],
        help_text=_("Priority from 0-999 to determine the sorting order."))

    objects = ContactManager()

    panels = [
        MultiFieldPanel([  
            FieldPanel('title', classname=''),
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ], heading='Name'),
        InlinePanel(
            'positions', label="Positions",
            panels=None),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('room'),
        InlinePanel(
            'groups', label="Groups",
            panels=None),
        FieldPanel('is_active'),
        FieldPanel('priority'),
    ]

    search_fields = [
        index.SearchField('first_name', partial_match=True),
        index.SearchField('last_name', partial_match=True),
        index.SearchField('email', partial_match=True),
        index.SearchField('phone'),
        index.SearchField('room'),
        index.FilterField('is_active')
        # index.SearchField('groups'),
    ]

    def __str__(self):
        if self.first_name and self.last_name:
            if self.title:
                return f'{self.title} {self.first_name} {self.last_name}'
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.email


    class Meta:  # noqa
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        # ordering = ['groups__group', '-priority', 'last_name']
        ordering = ['last_name']


@register_snippet
class Group(index.Indexed, ClusterableModel):
    slug = models.CharField(_("slug"), max_length=254)
    name = models.CharField(_("name"), max_length=254, blank=True)
    priority = models.PositiveSmallIntegerField(
        _("priority"), blank=True, default=0, validators=[MaxValueValidator(99)],
        help_text=_("Priority from 0-99 to determine the sorting order."))

    panels = [
        FieldPanel('name'),
        FieldPanel('priority'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
        index.SearchField('slug'),
    ]

    @property
    def members(self):
        return [relation.contact for relation in self.contacts.select_related('contact')]

    def __str__(self):
        return self.name or self.slug

    class Meta:  # noqa
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ['-priority']
