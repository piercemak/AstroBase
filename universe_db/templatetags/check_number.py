from django import template
from decimal import Decimal, getcontext

register = template.Library()

getcontext().prec = 10  # set the precision you want


@register.filter
def needs_sci_notation(value):
    d = Decimal(value)
    return d.adjusted() > 4 or (d.adjusted() < .001 and d != 0)


'''
@register.filter
def needs_sci_notation(value, measurement_type):
    d = Decimal(value)
    sci_fields = ['Distance', 'Perihelion', 'Aphelion']
    return d.adjusted() > 4 or (d.adjusted() < 0 and d != 0) or (measurement_type in sci_fields)
'''
