from django.views.generic.list import ListView

from .models import Contact


class ContactListView(ListView):
    model = Contact