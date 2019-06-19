from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import NewsPage, NewsEntry


@register(NewsPage)
class NewsPageTR(TranslationOptions):
    pass


@register(NewsEntry)
class NewsEntryTR(TranslationOptions):
    fields = (
        'body',
    )
