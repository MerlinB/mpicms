from django.utils.translation import gettext_lazy as _
from django.contrib.admin.utils import (quote, unquote)
from django.shortcuts import get_object_or_404

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.views import EditView, InspectView, DeleteView, InstanceSpecificView

from .models import Contact, Group, Position


class ContactInstanceView(InstanceSpecificView):
    def __init__(self, model_admin, instance_pk):
        super(InstanceSpecificView, self).__init__(model_admin)
        self.instance_pk = unquote(instance_pk)
        self.pk_quoted = quote(self.instance_pk)
        filter_kwargs = {}
        filter_kwargs[self.pk_attname] = self.instance_pk
        object_qs = model_admin.model._default_manager.include_inactive().filter(
            **filter_kwargs)
        self.instance = get_object_or_404(object_qs)

class ContactEditView(ContactInstanceView, EditView):
    pass

class ContactInspectView(ContactInstanceView, InspectView):
    pass

class ContactDeleteView(ContactInstanceView, DeleteView):
    pass

class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = _('Persons')
    menu_icon = 'user'
    list_display = ['title', 'first_name', 'last_name', 'position', 'email', 'phone', 'room', 'get_groups']
    list_filter = ['groups__group', 'is_active', 'position']
    search_fields = ['title', 'first_name', 'last_name', 'position__title', 'email', 'phone', 'room']

    edit_view_class = ContactEditView
    inspect_view_class = ContactInspectView
    delete_view_class = ContactDeleteView

    def get_groups(self, obj):
        return ", ".join([group.__str__() for group in Group.objects.filter(contacts__in=obj.groups.all()).distinct()])
    get_groups.short_description = _('Groups')

    def get_queryset(self, request):
        qs = self.model._default_manager.include_inactive()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


class GroupAdmin(ModelAdmin):
    model = Group
    menu_label = _('Groups')
    menu_icon = 'group'
    search_fields = 'name'


class PositionAdmin(ModelAdmin):
    model = Position
    menu_label = _('Positions')
    menu_icon = 'tag'
    search_fields = ['title']


class ContactGroup(ModelAdminGroup):
    menu_label = _('Contacts')
    menu_icon = 'user'
    items = [
        ContactAdmin,
        GroupAdmin,
        PositionAdmin
    ]


modeladmin_register(ContactGroup)
# modeladmin_register(ContactAdmin)
# modeladmin_register(GroupAdmin)
