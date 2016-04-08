# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def hash(obj, key):
    key, fallback_key = key.split(':') if ':' in key else (key, '')
    print key, fallback_key
    return getattr(obj, key, getattr(obj, fallback_key, None))


@register.simple_tag
def to_list(*args):
    return args


@register.simple_tag()
def breadcrumb(view, text, pk=None):
    kwargs = {'pk':pk } if pk else {}
    return mark_safe(u'» <a href="' + reverse(view, kwargs=kwargs) + '">' + text + '</a>')
