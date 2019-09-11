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
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from mpicms.news.mixins import NewsMixin
from mpicms.events.mixins import EventMixin
from .mixins import BasePage, BodyMixin, SideBarMixin
from .blocks import ContactBlock, MenuBlock


Page.show_in_menus_default = True


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).type(HomePage).order_by('-depth').first()

    class Meta:  # noqa
        abstract = True


@register_snippet
class FeaturedImage(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    title = models.CharField(_('title'), max_length=200, blank=True)
    text = RichTextField(_('text'), features=['bold', 'italic', 'link', 'document-link'])

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title

    class Meta:  # noqa
        verbose_name = _('featured image')
        verbose_name_plural = _('featured images')


class RootPage(EventMixin, NewsMixin, BasePage):
    featured_image = models.ForeignKey(
        'FeaturedImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('featured image')
    )
    banner = StreamField([
        ('banner', blocks.StructBlock([
            ('title', blocks.CharBlock(max_length=200, required=False, label=_('Title'))),
            ('text', blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label=_('Text')))
        ], icon='warning', label=_('Banner')))
    ], blank=True, verbose_name=_('Banner'))
    footer_items = StreamField([
        ('menu', MenuBlock())
    ], blank=True, verbose_name=_('Footer Items'))
    quick_links = StreamField([
        ('menu', MenuBlock())
    ], blank=True, verbose_name=_('Quick Links'))

    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root
    max_count = 1

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner'),
        SnippetChooserPanel('featured_image'),
        StreamFieldPanel('footer_items'),
        StreamFieldPanel('quick_links')
    ]

    api_fields = [
        # APIField('banner')
    ]

    class Meta: # noqa
        verbose_name = _("root page")
        verbose_name_plural = _("root pages")


class HomePage(NewsMixin, SideBarMixin, BodyMixin, BasePage):
    content_panels = Page.content_panels + BodyMixin.content_panels + SideBarMixin.content_panels
    search_fields = Page.search_fields + BodyMixin.search_fields + SideBarMixin.search_fields
    api_fields = BodyMixin.api_fields

    creation_limited = True  # limits creation to staff/superusers

    @property
    def category(self):
        return self

    class Meta: # noqa
        verbose_name = _("homepage")
        verbose_name_plural = _("homepages")


class WikiPage(CategoryMixin, SideBarMixin, BodyMixin, BasePage):
    content_panels = Page.content_panels + BodyMixin.content_panels + SideBarMixin.content_panels
    search_fields = Page.search_fields + BodyMixin.search_fields + SideBarMixin.search_fields
    api_fields = BodyMixin.api_fields

    class Meta: # noqa
        verbose_name = _("wiki page")
        verbose_name_plural = _("wiki pages")
