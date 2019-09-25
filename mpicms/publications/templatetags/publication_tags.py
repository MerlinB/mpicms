from django import template
from mpicms.publications.models import Publication

register = template.Library()


@register.inclusion_tag('publications/components/list.html', takes_context=True)
def publication_list(context):
    return {
        'publications': Publication.objects.all()[:5],
        'request': context['request'],
    }
