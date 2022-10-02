from django import template

register = template.Library()


# A custom tag to wrap and line break a=based on argument supplied in template
@register.filter(name='skills_filter')
def skills_filter(value):   
    
    value_list = (value.strip()).split(',')  
    
    value_dict = {}
    for vl in value_list:
        if vl:
            vl_list = (vl.split('='))            
            value_dict.update({vl_list[0].strip():vl_list[1].strip()})       
    
    return value_dict.items()