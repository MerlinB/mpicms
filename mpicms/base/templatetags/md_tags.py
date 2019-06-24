from markdown import markdown as md

from django import template


register = template.Library()


@register.filter
def markdown(text):
    return md(text=text)
