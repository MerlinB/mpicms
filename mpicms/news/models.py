from django.db import models
from django.utils.translation import gettext as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from mpicms.base.models import CategoryMixin


class NewsPage(CategoryMixin, Page):
    content_panels = Page.content_panels + [
        FieldPanel('show_all')
    ]
    show_all = models.BooleanField(default=False)

    parent_page_types = ['base.CategoryPage', 'base.HomePage']
    subpage_types = ['NewsEntry']
    show_in_menus_default = False

    @property
    def news_items(self):
        if self.show_all:
            return NewsEntry.objects.descendant_of(self.get_parent()).live().order_by('-date')
        return NewsEntry.objects.child_of(self).live().order_by('-date')


    class Meta:  # noqa
        verbose_name = _("news Blog")
        verbose_name_plural = _("news Blogs")


class NewsEntry(CategoryMixin, Page):
    preview = models.TextField(_("preview"), blank=True)
    body = RichTextField(_("content"))
    date = models.DateField("Post date", auto_now_add=True)

    content_panels = Page.content_panels + [
        FieldPanel('preview'),
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['NewsPage']

    class Meta:  # noqa
        verbose_name = _("news entry")
        verbose_name_plural = _("news entries")
