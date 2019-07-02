from django.shortcuts import render
from django.core.paginator import Paginator

from wagtail.core.models import Page
from wagtail.core import hooks
from wagtail.search.models import Query
from wagtail.admin.views.account import LogoutView as LView


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
