from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied

from wagtail.core.models import Page
from wagtail.core import hooks
from wagtail.search.models import Query
from wagtail.admin.views.account import LogoutView as LView
from wagtail.admin.views.pages import get_valid_next_url_from_request

from .utils import can_create


def search(request):
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    paginator = Paginator(search_results, 8)

    page = request.GET.get('page')
    search_results = paginator.get_page(page)

    return render(request, 'base/search_results.html', {
        'paginator': paginator,
        'search_query': search_query,
        'search_results': search_results,
    })


class LogoutView(LView):
    """Prevent error for unprevileged users when redirect to admin"""
    next_page = '/'


def account(request):
    """Override wagtail account view to remove email and password menu items"""

    items = []

    for fn in hooks.get_hooks('register_account_menu_item'):
        item = fn(request)
        if item:
            if any(excluded in item['url'] for excluded in ['change_email', 'change_password']):
                continue
            items.append(item)

    return render(request, 'wagtailadmin/account/account.html', {
        'items': items,
    })


def add_subpage(request, parent_page_id):
    """Override wagtail view to prevent creation of limited pages"""

    parent_page = get_object_or_404(Page, id=parent_page_id).specific
    if not parent_page.permissions_for_user(request.user).can_add_subpage():
        raise PermissionDenied

    page_types = [
        (model.get_verbose_name(), model._meta.app_label, model._meta.model_name)
        for model in type(parent_page).creatable_subpage_models()
        if model.can_create_at(parent_page) and can_create(request, model)
    ]
    # sort by lower-cased version of verbose name
    page_types.sort(key=lambda page_type: page_type[0].lower())

    if len(page_types) == 1:
        # Only one page type is available - redirect straight to the create form rather than
        # making the user choose
        verbose_name, app_label, model_name = page_types[0]
        return redirect('wagtailadmin_pages:add', app_label, model_name, parent_page.id)

    return render(request, 'wagtailadmin/pages/add_subpage.html', {
        'parent_page': parent_page,
        'page_types': page_types,
        'next': get_valid_next_url_from_request(request),
    })
