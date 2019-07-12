from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
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


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).type(HomePage).order_by('-depth').first()

    class Meta:  # noqa
        abstract = True


class RootPage(EventMixin, NewsMixin, BasePage):
    banner = StreamField([
        ('banner', blocks.StructBlock([
            ('title', blocks.CharBlock(max_length=200, required=False, label=_('Title'))),
            ('text', blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label=_('Text')))
        ], icon='warning', label=_('Banner')))
    ], blank=True, verbose_name=_('Banner'))
    footer_items = StreamField([
        ('menu', blocks.StructBlock([
            ('title', blocks.CharBlock(label=_('Title'))),
            ('items', blocks.ListBlock(
                blocks.StructBlock([
                    ('title', blocks.CharBlock(label=_('Title'))),
                    ('url', blocks.URLBlock(label=_('URL')))
                ], label=_('Items'))
            ))
        ], icon='list-ul', label=_('Menu')))
    ], blank=True, verbose_name=_('Footer Items'))

    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root
    max_count = 1

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner'),
        StreamFieldPanel('footer_items')
    ]

    api_fields = [
        # APIField('banner')
    ]

    class Meta: # noqa
        verbose_name = _("root page")
        verbose_name_plural = _("root pages")


class HomePage(NewsMixin, BodyMixin, BasePage):
    sidebar = StreamField([
        ('editor', blocks.RichTextBlock(
            features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'], label=_('Editor'))),
        ('contacts', blocks.ListBlock(
            blocks.StructBlock([
                ('contact', SnippetChooserBlock('personal.Contact', label=_("Contact"))),
                ('information', blocks.TextBlock(required=False, label=_('Information'))),
            ]), icon="user", template='base/blocks/contact_block.html', label=_('Contacts'))
        )
    ], blank=True, verbose_name=_("Sidebar Content"))

    content_panels = Page.content_panels + BodyMixin.content_panels + [
        StreamFieldPanel('sidebar'),
    ]

    search_fields = Page.search_fields + BodyMixin.search_fields + [
        index.SearchField('sidebar'),
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
