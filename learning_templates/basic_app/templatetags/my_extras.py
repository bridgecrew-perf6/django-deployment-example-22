from django import template

register = template.Library()

#Now goes function with your filter:
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,"")

register.filter("cut", cut) #(name_of_filter, name_of_function) - they do not have to be same
     
"""  
@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg,"")

"""  