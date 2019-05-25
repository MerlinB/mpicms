from django import template


register = template.Library()


@register.simple_tag
def is_ancestor(page, parent):
    return page.is_descendant_of(parent)
