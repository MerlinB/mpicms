from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views import defaults as default_views, static as static_views

from base.views import search


urlpatterns = [
    path('django-admin', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('search', search, name='search'),
    path('docs/', static_views.serve, {'document_root': settings.DOCS_ROOT, 'path': 'index.html'}, name='docs'),
    re_path('^docs/(?P<path>.*)$', static_views.serve, {'document_root': settings.DOCS_ROOT}),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    re_path(r'', include(wagtail_urls)),
)

if settings.DEBUG:
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
