from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import Position, Group


@register(Position)
class PositionTR(TranslationOptions):
    fields = (
        'title',
    )


@register(Group)
class GroupTR(TranslationOptions):
    fields = (
        'name',
    )
