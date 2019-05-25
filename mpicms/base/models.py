from django.db import models
from django.utils.translation import gettext as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock

from mpicms.news.models import NewsPage


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

    def get_context(self, request):
        context = super().get_context(request)
        context['news'] = NewsPage.objects.first()
        return context

    class Meta: # noqa
        verbose_name = _("homepage")
        verbose_name_plural = _("homepages")


class CategoryPage(Page):
    body = RichTextField(_("content"), blank=True)
    side_content = RichTextField(
        _("sidebar content"), blank=True,
        features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'],
        help_text=_("Information displayed on the page in the sidebar")
    )
    # contact = models.ManyToManyField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('side_content')
    ]

    parent_page_types = ['HomePage', 'CategoryPage']

    @property
    def category(self):
        return self

    class Meta: # noqa
        verbose_name = _("category")
        verbose_name_plural = _("categories")


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

