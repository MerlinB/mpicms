from django.db import models
from django.utils.translation import gettext as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class NewsPage(Page):
    content_panels = Page.content_panels

    parent_page_types = ['base.CategoryPage', 'base.HomePage']
    subpage_types = ['NewsEntry']
    show_in_menus_default = False

    class Meta:  # noqa
        verbose_name = _("news Blog")
        verbose_name_plural = _("news Blogs")


class NewsEntry(Page):
    preview = models.TextField(_("preview"), blank=True)
    body = RichTextField(_("content"))

    content_panels = Page.content_panels + [
        FieldPanel('preview'),
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['NewsPage']

    class Meta:  # noqa
        verbose_name = _("news entry")
        verbose_name_plural = _("news entries")
