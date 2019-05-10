from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    phone = forms.IntegerField(label=_("Phone"))
    office = forms.CharField(label=("Office"))


class CustomUserCreationForm(UserCreationForm):
    phone = forms.IntegerField(label=_("Phone"))
    office = forms.CharField(label=("Office"))
