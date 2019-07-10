from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import Position


@register(Position)
class PositionTR(TranslationOptions):
    fields = (
        'title',
    )
