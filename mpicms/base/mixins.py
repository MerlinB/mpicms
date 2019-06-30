from django.utils import translation
from django.conf import settings

from wagtail.core.models import Page


class BasePage(Page):
    """Enable multilingual preview capabilities"""

    preview_modes = settings.LANGUAGES

    def serve_preview(self, request, mode_name):
        translation.activate(mode_name)
        return super().serve_preview(request, mode_name)

    class Meta:  # noqa
        abstract = True
