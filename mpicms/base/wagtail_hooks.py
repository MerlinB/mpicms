from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.html import format_html
from django.templatetags.static import static
from django.contrib.auth import get_user_model

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.helpers import PermissionHelper


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
    return MenuItem(_('View website'), '/', classnames='icon icon-site', order=1)


@hooks.register('register_admin_menu_item')
def register_docs_link():
    return MenuItem(_('Documentation'), reverse('docs'), classnames='icon icon-help', order=10000)
