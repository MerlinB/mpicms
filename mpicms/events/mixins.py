from django.db import models

from .models import EventIndex


class EventMixin(models.Model):

    @property
    def event_index(self):
        return self.get_children().type(EventIndex).first()

    class Meta:  # noqa
        abstract = True
