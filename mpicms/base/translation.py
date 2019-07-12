"""Models are registered for translation here.

Due to the Page model being translated by wagtail-modeltranslation all child-models must be registered as well.
See https://github.com/infoportugal/wagtail-modeltranslation/pull/150.
"""

from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import WikiPage, RootPage, HomePage


@register(RootPage)
class RootPageTR(TranslationOptions):
    fields = {
        'footer_items'
    }

@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'body',
        'sidebar'
    )


@register(WikiPage)
class WikiPageTR(TranslationOptions):
    fields = (
        'body',
    )
