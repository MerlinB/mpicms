from django.views.generic.list import ListView

from .models import Contact


class ContactListView(ListView):
    model = Contact
    
    def get_queryset(self):
        return Contact.objects.is_active().order_by('last_name')