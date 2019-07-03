from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from mpicms.news.mixins import NewsMixin
from mpicms.events.mixins import EventMixin
from .mixins import BasePage, BodyMixin


Page.show_in_menus_default = True


@register_snippet
class Banner(models.Model):
    title = models.CharField(_('title'), max_length=200, blank=True)
    text = RichTextField(_('text'), features=['bold', 'italic', 'link', 'document-link'])

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title

    class Meta:  # noqa
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).type(HomePage).order_by('-depth').first()

    class Meta:  # noqa
        abstract = True


class RootPage(EventMixin, NewsMixin, BasePage):
    banner = models.ForeignKey(
        'Banner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('banner')
    )

    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root
    max_count = 1

    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
    ]

    api_fields = [
        APIField('banner')
    ]

    class Meta: # noqa
        verbose_name = _("root page")
        verbose_name_plural = _("root pages")


class HomePage(NewsMixin, BodyMixin, BasePage):
    sidebar = StreamField([
        (_('Editor'), blocks.RichTextBlock(
            features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'])),
        (_('Contacts'), blocks.ListBlock(
            blocks.StructBlock([
                ('contact', SnippetChooserBlock('personal.Contact', label="Contact")),
                ('information', blocks.TextBlock(required=False)),
            ]), icon="user")
        )
    ], blank=True, verbose_name=_("sidebar content"))

    content_panels = Page.content_panels + BodyMixin.content_panels + [
        StreamFieldPanel('sidebar'),
    ]

    search_fields = Page.search_fields + BodyMixin.search_fields + [
        index.SearchField('side_content'),
    ]

    api_fields = BodyMixin.api_fields

    creation_limited = True  # limits creation to staff/superusers

    @property
    def category(self):
        return self

    class Meta: # noqa
        verbose_name = _("homepage")
        verbose_name_plural = _("homepages")


class WikiPage(CategoryMixin, BodyMixin, BasePage):
    search_fields = Page.search_fields + BodyMixin.content_panels
    content_panels = Page.content_panels + BodyMixin.content_panels
    api_fields = BodyMixin.api_fields

    class Meta: # noqa
        verbose_name = _("wiki page")
        verbose_name_plural = _("wiki pages")
