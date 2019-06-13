from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_json_events(context, event_index):
    return event_index.get_json_events(request=context['request'])
