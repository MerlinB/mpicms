from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import ugettext as _

from wagtail.admin import messages
from wagtail.admin.utils import permission_required
from wagtail.core import hooks

from wagtail.users.views.users import User, change_user_perm, get_user_edit_form


@permission_required(change_user_perm)
def edit(request, user_id):
    """Override wagtail user edit view to prevent changes"""
    user = get_object_or_404(User, pk=user_id)
    can_delete = False
    editing_self = request.user == user

    for fn in hooks.get_hooks('before_edit_user'):
        result = fn(request, user)
        if hasattr(result, 'status_code'):
            return result
    if request.method == 'POST':
        form = get_user_edit_form()(request.POST, request.FILES, instance=user, editing_self=editing_self)
        if form.is_valid():
            user = form.save()

            if user == request.user and 'password1' in form.changed_data:
                # User is changing their own password; need to update their session hash
                update_session_auth_hash(request, user)

            messages.success(request, _("User '{0}' updated.").format(user), buttons=[
                messages.button(reverse('wagtailusers_users:edit', args=(user.pk,)), _('Edit'))
            ])
            for fn in hooks.get_hooks('after_edit_user'):
                result = fn(request, user)
                if hasattr(result, 'status_code'):
                    return result
            return redirect('wagtailusers_users:index')
        else:
            messages.error(request, _("The user could not be saved due to errors."))
    else:
        form = get_user_edit_form()(instance=user, editing_self=editing_self)

    return render(request, 'wagtailusers/users/edit.html', {
        'user': user,
        'form': form,
        'can_delete': can_delete,
    })
