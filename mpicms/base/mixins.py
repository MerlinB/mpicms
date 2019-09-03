from django.utils import translation
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _, get_language_info
from django.contrib.auth import get_user_model
from django.contrib import messages

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.api import APIField

from mpicms.base.serializers import OptionalStreamField

from .blocks import ContentBlock


class BasePage(Page):
    subscribers = models.ManyToManyField(get_user_model())

    # Enable multilingual preview capabilities
    preview_modes = settings.LANGUAGES

    def serve_preview(self, request, mode_name):
        translation.activate(mode_name)
        return super().serve_preview(request, mode_name)

    def serve(self, request):  # Not in use
        if request.user.is_authenticated:
            if 'subscribe' in request.GET:
                self.subscribers.add(request.user)
            elif 'unsubscribe' in request.GET:
                self.subscribers.remove(request.user)

        return super().serve(request)

    class Meta:  # noqa
        abstract = True


class BodyMixin(Page):
    body = StreamField(ContentBlock(), blank=True, verbose_name=_('content'))

    content_panels = [
        StreamFieldPanel('body'),
    ]

    search_fields = [
        index.SearchField('body'),
    ]

    api_fields = [
        APIField('body', serializer=OptionalStreamField()),
    ]

    @property
    def preview_text(self):
        if self.search_description:
            return self.search_description
        elif self.body:
            first_block = next(iter(self.body), None)
            return first_block if first_block.block_type in [
                'richtext',
                'markdown'
            ] else None

    def serve(self, request):
        lang = request.LANGUAGE_CODE
        if not getattr(self, 'body_' + lang) and self.body:
            messages.info(request, _('Page not available in ') + get_language_info(lang)['name_local'])

        return super().serve(request)

    class Meta:  # noqa
        abstract = True
