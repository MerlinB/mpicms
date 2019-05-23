from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock


class NewsPage(Page):
    content_panels = Page.content_panels

    child_page_types = ['NewsEntry']


class NewsEntry(Page):
    preview = models.TextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('url', blocks.URLBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('preview'),
        StreamFieldPanel('body', classname="full"),
    ]

    parent_page_types = ['NewsPage']