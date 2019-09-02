from django.views.generic.list import ListView
from django.db.models import OuterRef, Subquery

from .models import Contact, Group, ContactGroups


class ContactListView(ListView):
    model = Contact

    def get_queryset(self):
        group_pk = self.request.GET.get('group')
        if group_pk:
            members = Group.objects.get(pk=group_pk).members
            return super().get_queryset().filter(pk__in=[member.pk for member in members])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class RawContactListView(ContactListView):
    template_name = 'personal/contact_list_raw.html'
