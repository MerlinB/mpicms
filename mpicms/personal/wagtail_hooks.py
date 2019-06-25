from django.utils.translation import gettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.contrib.modeladmin.helpers import PermissionHelper

from .models import Contact, Group


class ReadOnlyPermissionHelper(PermissionHelper):

    def user_can_create(self, user):
        """
        Return a boolean to indicate whether `user` is permitted to create new
        instances of `self.model`
        """
        return False

    def user_can_edit_obj(self, user, obj):
        """
        Return a boolean to indicate whether `user` is permitted to 'change'
        a specific `self.model` instance.
        """
        return False

    def user_can_delete_obj(self, user, obj):
        """
        Return a boolean to indicate whether `user` is permitted to 'delete'
        a specific `self.model` instance.
        """
        return False


class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contacts'
    menu_icon = 'user'
    list_display = ['name', 'email', 'phone', 'room', 'get_groups']
    list_filter = ['groups']
    search_fields = ['name', 'email', 'phone', 'room']

    def get_groups(self, obj):
        return ", ".join([group.__str__() for group in obj.groups.all()])
    get_groups.short_description = _('Groups')

    readonly_fields = ['name']
    permission_helper_class = ReadOnlyPermissionHelper


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
