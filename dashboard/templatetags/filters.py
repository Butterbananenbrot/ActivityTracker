from django import template

register = template.Library()

@register.filter
def reverse_str(value):
    return value[::-1]

@register.filter
def filter_keys(key):
    key = key.replace("_", " ")
    key = key.title()
    return key