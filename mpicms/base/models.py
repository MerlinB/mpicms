from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock

from .behaviours import CategoryMixin


Page.show_in_menus_default = True


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root

    content_panels = Page.content_panels


class CategoryPage(CategoryMixin, Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['HomePage', 'CategoryPage']


class WikiPage(CategoryMixin, Page):
    body = RichTextField()
    date = models.DateField("Post date", auto_now_add=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]


class StreamPage(CategoryMixin, Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]
