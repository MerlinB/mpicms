from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock



Page.show_in_menus_default = True


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).type(CategoryPage).order_by('-depth').first()

    class Meta:
        abstract = True


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root

    content_panels = Page.content_panels


class CategoryPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('url', blocks.URLBlock())
    ], blank=True)
    side_content = StreamField([
        ('information', blocks.StructBlock([
                ('heading', blocks.CharBlock(classname="full title")),
                ('content', blocks.TextBlock()),
        ], icon="list-ul"))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
        StreamFieldPanel('side_content')
    ]

    parent_page_types = ['HomePage', 'CategoryPage']

    @property
    def category(self):
        return self


class WikiPage(CategoryMixin, Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('url', blocks.URLBlock())
    ], blank=True)
    date = models.DateField("Post date", auto_now_add=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
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
