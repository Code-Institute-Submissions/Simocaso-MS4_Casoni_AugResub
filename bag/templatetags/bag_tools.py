from django import template


register = template.Library()


@register.filter(name='prd_subtotal')
def prd_subtotal(price, quantity):
    return price * quantity
