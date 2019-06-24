import json
from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField

from base.blocks import ContentBlock


class Event(Page):
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'), blank=True, null=True)
    start_time = models.TimeField(_('start time'), blank=True, null=True)
    end_time = models.TimeField(_('end time'), blank=True, null=True)
    description = models.TextField(_('description'), max_length=400, null=False, blank=True)
    body = StreamField(ContentBlock, blank=True, verbose_name=_('content'))

    show_in_menus_default = False
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
            heading=_('event dates')
        ),
        StreamFieldPanel('body'),
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


class EventIndex(Page):
    parent_page_types = ['base.RootPage']
    subpage_types = ['events.Event']

    @property
    def events(self):
        if self.depth <= 3:
            return Event.objects.live().specific()
        return self.get_children().stype(Event).live().specific()

    def get_json_events(self, request=None):
        event_dicts = [event.get_dict(request) for event in self.events]
        return json.dumps(event_dicts)

    def clean(self):  # Prevent more than one event index
        model = self.__class__
        if (model.objects.count() > 0 and self.pk != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)

    class Meta:  # noqa
        verbose_name = _('event index')
        verbose_name_plural = _('event indexes')
