from django.shortcuts import render
from django.core.paginator import Paginator

from wagtail.core.models import Page
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
    next_page = '/'
