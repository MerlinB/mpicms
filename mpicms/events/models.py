import json
from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
# from wagtail.images.blocks import ImageChooserBlock
# from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

# from .date_filters import get_range
# from .managers import DatedEventManager
# from .utils import date_to_datetime


class Event(Page):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    # objects = DatedEventManager()
    description = models.TextField(max_length=400, null=False, blank=True)
    body = RichTextField(_("content"), blank=True)

    parent_page_types = ['events.EventIndex']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        MultiFieldPanel(
            [
                FieldPanel('start_date'),
                FieldPanel('start_time'),
                FieldPanel('end_date'),
                FieldPanel('end_time'),
            ],
            heading="Event Start / End Dates"
        ),
        FieldPanel('body', classname="full"),
    ]

    @property
    def start(self):
        if self.start_time:
            return datetime.combine(self.start_date, self.start_time)
        return self.start_date

    @property
    def end(self):
        if self.end_time:
            return datetime.combine(self.end_date, self.end_time)
        return self.end_date

    def clean(self):
        """Clean the model fields, if end_date is before start_date raise a ValidationError."""
        super().clean()

        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'The end date cannot be before the start date.'})

    class Meta(object):  # noqa
        ordering = ['start_date']


class EventIndex(Page):
    parent_page_types = ['base.HomePage']
    subpage_types = ['events.Event']

    # PAGINATE_BY = 3

    # search_fields = Page.search_fields + [
    #     index.SearchField('body'),
    #     index.FilterField('date'),
    # ]

    content_panels = Page.content_panels
    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    # ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        events = []
        for child in self.get_children().type(Event).live().specific():
            events.append({
                'title': child.title,
                'start': child.start.isoformat(),
                'end': child.end.isoformat(),
                'url': child.get_url(request=request),
                'color': '#006c66'
            })

        context["events"] = json.dumps(events)

        return context


    # def get_context(self, request, *args, **kwargs):
    #     """
    #     Adds child pages to the context and paginates them.
    #     """
    #     context = super().get_context(request, *args, **kwargs)
    #     children = self.get_children().type(Event)

    #     # Period
    #     period = request.GET.get('scope', None)
    #     start_date = request.GET.get('start_date', '')
    #     if period:
    #         self.get_start_end(period, start_date)
    #     children.filter(start_date__gte=start_date).filter(end_date__lte=end_date)

    #     # Pagination
    #     paginator = Paginator(queryset, PAGINATE_BY)
    #     page_num = request.GET.get('page', 1) or 1

    #     try:
    #         queryset = paginator.page(page_num)
    #     except PageNotAnInteger:
    #         queryset = paginator.page(1)
    #     except EmptyPage:
    #         queryset = paginator.page(paginator.num_pages)

    #     context.update(
    #         children=queryset,
    #         paginator=paginator
    #     )
    #     return context
