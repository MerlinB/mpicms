from django.utils.translation import gettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.contrib.modeladmin.helpers import PermissionHelper

from .models import Contact, Group


class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contacts'
    menu_icon = 'user'
    list_display = ['title', 'first_name', 'last_name', 'position', 'email', 'phone', 'room', 'get_groups']
    list_filter = ['groups__group', 'is_active']
    search_fields = ['title', 'first_name', 'last_name', 'position', 'email', 'phone', 'room']

    def get_groups(self, obj):
        return ", ".join([group.__str__() for group in Group.objects.filter(contacts__in=obj.groups.all()).distinct()])
    get_groups.short_description = _('Groups')
    

class GroupAdmin(ModelAdmin):
    model = Group
    menu_label = 'Groups'
    menu_icon = 'group'
    search_fields = 'name'


class ContactGroup(ModelAdminGroup):
    menu_label = 'Phone List'
    items = [ContactAdmin, GroupAdmin]


modeladmin_register(ContactAdmin)
modeladmin_register(GroupAdmin)
