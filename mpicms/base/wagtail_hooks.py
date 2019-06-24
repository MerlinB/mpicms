from wagtail.core import hooks
# from django.contrib.auth.models import Permission


# @hooks.register('register_permissions')
# def get_page_permissions():
#     return Permission.objects.filter(codename__contains="homepage")


@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    features.default_features.insert(0, 'h1')
