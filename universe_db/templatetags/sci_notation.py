from django import template

register = template.Library()

@register.filter
def sci_notation(value):
    return "{:.2e}".format(value)
