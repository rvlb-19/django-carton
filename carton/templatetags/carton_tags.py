from django import template

from carton.cart import Cart
from carton.settings import CART_TEMPLATE_TAG_NAME

register = template.Library()
register_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag

def get_cart(context, session_key=None, cart_class=Cart):
    """
    Make the cart object available in template.

    Sample usage::

        {% load carton_tags %}
        {% get_cart as cart %}
        {% for product in cart.products %}
            {{ product }}
        {% endfor %}
    """
    request = context['request']
    return cart_class(request.session, session_key=session_key)

register_tag(takes_context=True, name=CART_TEMPLATE_TAG_NAME)(get_cart)
