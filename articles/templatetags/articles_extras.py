from django import template

register = template.Library()

@register.filter(name="date_format")
def date_format(value):
    if value:
        return value.strftime("%m/%d/%Y")
    return ""