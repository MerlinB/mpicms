from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.search import index
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel

from mpicms.base.models import CategoryMixin
from mpicms.base.mixins import BasePage, BodyMixin


class NewsPage(CategoryMixin, BasePage):
    content_panels = Page.content_panels
    parent_page_types = ['base.HomePage', 'base.RootPage']
    subpage_types = ['NewsEntry']
    paginated_by = 8

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if self.is_news_root:
            context['blogs'] = NewsPage.objects.all()

        paginator = Paginator(self.news_items, self.paginated_by)

        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['paginator'] = paginator
        context["news_items"] = posts
        return context

    @property
    def is_news_root(self):
        return self.depth <= 3

    @property
    def news_items(self):
        items = NewsEntry.objects.child_of(self).live().order_by('-date')
        if self.is_news_root:
            imported_news = NewsEntry.objects.live().filter(show_in_main_news=True)
            combined_items = list(items) + list(imported_news)
            items = sorted(combined_items, key=lambda x: x.date, reverse=True)
        return items


    class Meta:  # noqa
        verbose_name = _("news blog")
        verbose_name_plural = _("news blogs")


class NewsEntry(CategoryMixin, BodyMixin, BasePage):
    date = models.DateField(_("date"), default=date.today)
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_in_main_news = models.BooleanField(default=False)

    show_in_menus_default = False

    content_panels = Page.content_panels + BodyMixin.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('header_image'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('show_in_main_news')
    ]

    search_fields = Page.search_fields + BodyMixin.search_fields + [
        index.FilterField('date')
    ]

    api_fields = BodyMixin.api_fields + [
        APIField('date')
    ]

    parent_page_types = ['NewsPage']

    class Meta:  # noqa
        ordering = ['-date']
        verbose_name = _("news entry")
        verbose_name_plural = _("news entries")
