from django.urls import re_path
from django.views import defaults as default_views

from wagtail.users.views import users

from .views import edit


app_name = 'wagtailusers_users'
urlpatterns = [
    re_path(r'^$', users.index, name='index'),
    re_path(r'^add/$', default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")}, name='add'),
    re_path(r'^([^\/]+)/$', edit, name='edit'),
    re_path(r'^([^\/]+)/delete/$', default_views.page_not_found, name='delete'),
]
