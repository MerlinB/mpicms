from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet

from modelcluster.models import ClusterableModel


@register_snippet
class Publication(index.Indexed, ClusterableModel):
    title = RichTextField(_('title'), features=['bold', 'italic', 'link'])
    groups = RichTextField(_('groups'), features=['bold', 'italic', 'link'], blank=True)
    authors = RichTextField(_('authors'), features=['bold', 'italic', 'link'], blank=True)
    source = RichTextField(_('source'), features=['bold', 'italic', 'link'], blank=True)
    doi = models.CharField("Digital Object Identifier", max_length=100, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('groups'),
        FieldPanel('authors'),
        FieldPanel('source'),
        FieldPanel('doi'),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True),
        index.SearchField('groups', partial_match=True),
        index.SearchField('authors', partial_match=True),
        index.SearchField('source', partial_match=True),
        index.SearchField('doi', partial_match=True),
    ]

    @property
    def link(self):
        return 'https://dx.doi.org/' + self.doi

    def __str__(self):
        return f'{strip_tags(self.title)} ({strip_tags(self.authors)})'

    class Meta:  # noqa
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
