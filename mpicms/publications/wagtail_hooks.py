from django.utils.translation import gettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Publication


class PublicationAdmin(ModelAdmin):
    model = Publication
    menu_label = _('Publications')
    menu_icon = 'doc-full'
    search_fields = ['title', 'auhtors', 'source', 'doi', 'groups']


modeladmin_register(PublicationAdmin)
