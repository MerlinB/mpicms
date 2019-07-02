from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.helpers import PermissionHelper

# from django.contrib.auth.models import Permission

from .models import Banner


# @hooks.register('register_permissions')
# def get_page_permissions():
#     return Permission.objects.filter(codename__contains="homepage")


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



class BannerAdmin(ModelAdmin):
    model = Banner
    menu_label = _('Banner')
    menu_icon = 'bold'


modeladmin_register(BannerAdmin)
