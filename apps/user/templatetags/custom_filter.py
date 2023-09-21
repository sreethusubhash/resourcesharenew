from django import template

register = template.Library()
@register.filter
def cap_all_but_upper_first(value):
#def cap_all_but_upper_first(value, arg):
    if value=='admin':
        return value.upper()
    else:
        return value.capitalize()
    
    