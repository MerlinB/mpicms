import logging

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html
from django.templatetags.static import static
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

from .models import FeaturedImage


logger = logging.getLogger(__name__)


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/admin.css'))


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    """Snippets are hidden so we can utilize ModelAdmin instead."""
    menu_items[:] = [item for item in menu_items if 'snippets' not in item.url]


@hooks.register('register_rich_text_features')
def register_h1_feature(features):
    """h1 headings should be allowed in rich text, as they can be used in markdown anyway."""
    features.default_features.insert(0, 'h1')


@hooks.register('register_admin_menu_item')
def register_site_button():
    return MenuItem(_('View website'), '/?', classnames='icon icon-site', order=1)  # Without the ? Wagtail applies different CSS 


@hooks.register('register_admin_menu_item')
def register_docs_link():
    return MenuItem(_('Documentation'), reverse('docs'), classnames='icon icon-help', order=10000)


@hooks.register('after_edit_page')
def send_notifications(request, page):
    subscribers = [user.email for user in page.subscribers.exclude(id=request.user.id)]

    if subscribers:
        html_message = f'''<a href="{request.build_absolute_uri(reverse('wagtailadmin_pages:revisions_index', args=[page.id]))}">View changes</a>\n
Edited by {request.user}.
You are receiving this message because you subscribed to updates for page {page.get_admin_display_title()}.
Log in to the admin interface and click <a href="{request.build_absolute_uri(reverse('wagtailadmin_pages_unsubscribe', args=[page.id]))}">here</a> to unsubscribe.'''

        send_mail(
            f'Page {page.get_admin_display_title()} edited.',
            strip_tags(html_message),
            settings.DEFAULT_FROM_EMAIL,
            subscribers,
            html_message=html_message,
            fail_silently=True)
        logger.debug(f'Send change notification to {subscribers}')


class FeaturedImageAdmin(ModelAdmin):
    model = FeaturedImage
    menu_label = _('Featured Images')
    menu_icon = 'image'


modeladmin_register(FeaturedImageAdmin)
