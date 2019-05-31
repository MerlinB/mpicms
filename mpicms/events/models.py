from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.blocks import CharBlock, TextBlock, BlockQuoteBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from .mixins import AbstractEvent, AbstractPaginatedIndex
# from .utils import _DATE_FORMAT_RE

import datetime
import re
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.utils import timezone
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page

from .date_filters import get_day_range, get_month_range, get_week_range, get_year_range
from .managers import DatedEventManager
from .utils import date_to_datetime


class Event(Page):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    objects = DatedEventManager()
    description = models.TextField(max_length=400, help_text='Briefly describe your event', null=False, blank=True)
    body = RichTextField(_("content"), blank=True)

    parent_page_types = ['events.EventIndex']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        MultiFieldPanel(
            [
                FieldPanel('start_date'),
                FieldPanel('end_date'),
            ],
            heading="Event Start / End Dates"
        ),
        FieldPanel('body', classname="full"),
    ]

    def clean(self):
        """Clean the model fields, if end_date is before start_date raise a ValidationError."""
        super().clean()

        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'The end date cannot be before the start date.'})

    class Meta(object):  # noqa
        ordering = ['start_date']


class EventIndex(Page):
    parent_page_types = []
    subpage_types = ['events.Event']

    PAGINATE_BY = 3

    def get_context(self, request, *args, **kwargs):
        """
        Adds child pages to the context and paginates them.
        """
        context = super().get_context(request, *args, **kwargs)
        children = self.get_children().type(Event)

        # Period
        period = request.GET.get('scope', None)
        start_date = request.GET.get('start_date', '')
        if period:
            self.get_start_end(period, start_date)
        children.filter(start_date__gte=start_date).filter(end_date__lte=end_date)

        # Pagination
        paginator = Paginator(queryset, PAGINATE_BY)
        page_num = request.GET.get('page', 1) or 1

        try:
            queryset = paginator.page(page_num)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context.update(
            children=queryset,
            paginator=paginator
        )
        return context