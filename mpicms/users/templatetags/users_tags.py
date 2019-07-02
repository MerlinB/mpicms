import itertools

from django import template

from wagtail.core import hooks

register = template.Library()


@register.inclusion_tag("wagtailadmin/pages/listing/_buttons.html",
                        takes_context=True)
def user_listing_buttons(context, user):
    """Override of wagtail function to remove delete button"""
    button_hooks = hooks.get_hooks('register_user_listing_buttons')
    buttons = sorted(itertools.chain.from_iterable(
        hook(context, user)
        for hook in button_hooks))
    buttons = [button for button in buttons if 'delete' not in button.url]
    return {'user': user, 'buttons': buttons}
