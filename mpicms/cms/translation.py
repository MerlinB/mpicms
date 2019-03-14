from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from .models import BlogPage


@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'body',
    )
