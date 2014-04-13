from django import template

register = template.Library()

@register.filter(name='get')
def get(d, k):
    return d.get(k, None)

@register.filter(name='pct')
def pct(val):
    return val * 100

