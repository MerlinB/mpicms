import json
from ics import Calendar, Event as ICSEvent
from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.api import APIField

from mpicms.base.mixins import BasePage, BodyMixin


class Event(BodyMixin, BasePage):
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'), blank=True, null=True)
    start_time = models.TimeField(_('start time'), blank=True, null=True)
    end_time = models.TimeField(_('end time'), blank=True, null=True)
    room = models.CharField(_('Room'), max_length=10, blank=True)

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_in_menus_default = False
    parent_page_types = ['events.EventIndex']
    subpage_types = []

    content_panels = Page.content_panels + BodyMixin.content_panels + [
        ImageChooserPanel('header_image'),
        MultiFieldPanel(
            [
                FieldPanel('start_date'),
                FieldPanel('start_time'),
                FieldPanel('end_date'),
                FieldPanel('end_time'),
            ],
            heading=_('event dates')
        ),
        FieldPanel('room')
    ]
    promote_panels = Page.promote_panels + BodyMixin.promote_panels

    api_fields = BodyMixin.api_fields + [
        APIField('start_date'),
        APIField('end_date'),
        APIField('start_time'),
        APIField('end_time'),
        APIField('room')
    ]

    @property
    def start(self):
        if self.start_time:
            return datetime.combine(self.start_date, self.start_time)
        return self.start_date

    @property
    def end(self):
        if self.end_time:
            date = self.end_date or self.start_date
            return datetime.combine(date, self.end_time)
        return self.end_date

    def get_dict(self, request=None):
        return {
            'title': self.title,
            'start': self.start.isoformat(),
            'end': self.end.isoformat() if self.end else None,
            'url': self.get_url(request=request),
            'color': '#006c66'
        }

    def clean(self):
        """Clean the model fields, if end_date is before start_date raise a ValidationError."""
        super().clean()

        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'The end date cannot be before the start date.'})

        if self.end_time and not self.start_time:
            raise ValidationError({'end_time': 'The end time cannot be set without a start time.'})

        if self.end and self.end < self.start:
            raise ValidationError({'end_time': 'The end time cannot be before the start time.'})

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        events = []
        for child in self.get_parent().get_children().type(Event).live().specific():
            events.append(child.get_dict(request))

        context["events"] = json.dumps(events)

        return context

    class Meta(object):  # noqa
        ordering = ['start_date']
        verbose_name = _('event')
        verbose_name_plural = _('events')


class EventIndex(BasePage):
    parent_page_types = ['base.RootPage']
    subpage_types = ['events.Event']

    @property
    def events(self):
        if self.depth <= 3:
            return Event.objects.live().specific()
        return self.get_children().type(Event).live().specific()

    def get_json_events(self, request=None):
        event_dicts = [event.get_dict(request) for event in self.events]
        return json.dumps(event_dicts)

    def clean(self):  # Prevent more than one event index
        model = self.__class__
        if (model.objects.count() > 0 and self.pk != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)

    @property
    def ics(self):
        c = Calendar()
        for event in self.events:
            print(event.url)
            e = ICSEvent(
                name = event.title,
                begin = event.start,
                end = event.end,
                description = event.search_description,
                url = event.full_url,
                location = event.room
            )
            c.events.add(e)
        return '\n'.join(c)


    class Meta:  # noqa
        verbose_name = _('event index')
        verbose_name_plural = _('event indexes')
