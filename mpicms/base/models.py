import json
from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from mpicms.news.mixins import NewsMixin
from mpicms.events.models import Event, EventIndex


Page.show_in_menus_default = True


@register_snippet
class Banner(models.Model):
    title = models.CharField(_('title'), max_length=200, blank=True)
    text = RichTextField(_('text'), features=['bold', 'italic', 'link', 'document-link'])

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title

    class Meta:  # noqa
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ContactRelation(Orderable, models.Model):
    """
    This defines the relationship between the `Contact` within the `personal`
    app and the CategoryPage below. This allows People to be added to the contact field.
    """
    page = ParentalKey(
        'CategoryPage', related_name=_('contacts'), on_delete=models.CASCADE
    )
    contact = models.ForeignKey(
        'personal.Contact',
        related_name='contact_references',
        on_delete=models.CASCADE,
        verbose_name=_('contact')
    )
    position = models.CharField(max_length=50, blank=True)

    panels = [
        SnippetChooserPanel('contact'),
        FieldPanel('position')
    ]

    class Meta:  # noqa
        verbose_name = _('contact information')
        verbose_name_plural = _('contact information')


class CategoryMixin(models.Model):
    @property
    def category(self):
        return Page.objects.ancestor_of(self, inclusive=True).type(CategoryPage).order_by('-depth').first()

    class Meta:  # noqa
        abstract = True


class HomePage(NewsMixin, Page):
    banner = models.ForeignKey(
        'Banner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('banner')
    )

    parent_page_types = ['wagtailcore.Page']  # Restrict parent to be root

    content_panels = Page.content_panels + [
        SnippetChooserPanel('banner'),
    ]

    @property
    def categories(self):
        return self.get_children().type(CategoryPage).live()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Events
        events = []
        for event in Event.objects.live():
            events.append(event.get_dict(request))

        context["events"] = json.dumps(events)
        context['event_index'] = EventIndex.objects.get()

        return context

    class Meta: # noqa
        verbose_name = _("homepage")
        verbose_name_plural = _("homepages")


class CategoryPage(NewsMixin, Page):
    preview = models.TextField(
        _("preview"), blank=True,
        help_text=_("Short description of this category")
    )
    body = RichTextField(_("content"), blank=True)
    side_content = RichTextField(
        _("sidebar content"), blank=True,
        features=['h4', 'h5', 'h6', 'bold', 'italic', 'link', 'document-link'],
        help_text=_("Text displayed in the sidebar of all child pages")
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('preview'),
        FieldPanel('side_content'),
        InlinePanel(
            'contacts', label="Contacts",
            panels=None),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('preview'),
        index.SearchField('side_content'),
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

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

    class Meta: # noqa
        verbose_name = _("wiki page")
        verbose_name_plural = _("wiki pages")

