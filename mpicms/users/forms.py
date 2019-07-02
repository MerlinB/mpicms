from django import forms

from wagtail.users.forms import (
    UserEditForm as WagtailUserEditForm,
    standard_fields,
    custom_fields,
    User
)


# from django import forms
# from django.utils.translation import ugettext_lazy as _

# from wagtail.users.forms import UserEditForm, UserCreationForm


# class CustomUserEditForm(UserEditForm):
#     phone = forms.IntegerField(label=_("Phone"))
#     office = forms.CharField(label=("Office"))


# class CustomUserCreationForm(UserCreationForm):
#     phone = forms.IntegerField(label=_("Phone"))
#     office = forms.CharField(label=("Office"))


class UserEditForm(WagtailUserEditForm):
    password_required = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['email'].disabled = True
        self.fields['username'].disabled = True

    class Meta:
        model = User
        fields = set([User.USERNAME_FIELD, "is_active"]) | standard_fields | custom_fields
        widgets = {
            'groups': forms.CheckboxSelectMultiple
        }
