from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.api import APIField

from mpicms.base.models import CategoryMixin

from base.blocks import ContentBlock
from base.serializers import OptionalStreamField


class NewsPage(CategoryMixin, Page):
    content_panels = Page.content_panels
    parent_page_types = ['base.HomePage', 'base.RootPage']
    subpage_types = ['NewsEntry']
    paginated_by = 8

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

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
    def news_items(self):
        if self.depth <= 3:
            return NewsEntry.objects.live().order_by('-date')
        return NewsEntry.objects.child_of(self).live().order_by('-date')


    class Meta:  # noqa
        verbose_name = _("news blog")
        verbose_name_plural = _("news blogs")


class NewsEntry(CategoryMixin, Page):
    body = StreamField(ContentBlock, blank=True, verbose_name=_('content'))
    date = models.DateField(_("post date"), auto_now_add=True)

    show_in_menus_default = False

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date')
    ]

    api_fields = [
        APIField('body', serializer=OptionalStreamField()),
        APIField('date')
    ]

    parent_page_types = ['NewsPage']

    class Meta:  # noqa
        ordering = ['-date']
        verbose_name = _("news entry")
        verbose_name_plural = _("news entries")
