from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import Event, EventIndex


@register(Event)
class EventPageTR(TranslationOptions):
    fields = [
        'body'
    ]


@register(EventIndex)
class EventIndexPageTR(TranslationOptions):
    pass
