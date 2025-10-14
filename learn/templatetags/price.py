from django import  template

register = template.Library()

@register.filter(name='point')
def point(value):
    formatted = f"{value:,}"
    return formatted

