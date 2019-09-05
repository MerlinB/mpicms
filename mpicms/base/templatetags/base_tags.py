from django import template

from mpicms.base.utils import get_room_link


register = template.Library()


@register.simple_tag
def is_ancestor(page, parent):
    return page.is_descendant_of(parent)


@register.simple_tag
def is_subscribed(page, user):
    return user in page.subscribers.all()


@register.simple_tag
def room_link(room):
    return get_room_link(room)