from django import template
from django.template import Variable, VariableDoesNotExist

register = template.Library()

@register.filter
def obj_hash(value, arg):
    return value[arg]
