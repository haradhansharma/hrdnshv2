from django.conf import settings
from django.urls import reverse

def looking_list():
    look_list = list((dict(settings.LOOKING)).keys())
    while("" in look_list) :
        look_list.remove("")    
    return look_list


def site_info():
    from common.models import ExSite  
       
    site = ExSite.on_site.get()   
    site_info = {
        'name' : site.site.name,
        'domain' : site.site.domain, 
        'canonical' : reverse('home:home'),
        'meta_name': site.site_meta,
        'description': site.site_description,
        'tag': site.site_meta_tag,
        'favicon': site.site_favicon.url,
        'mask_icon': site.mask_icon.url,
        'logo': site.site_logo.url,
        'slogan': site.slogan,
        'og_image': site.og_image.url,
        'phone': site.phone,
        'email': site.email,
        'location': site.location,
        'topic' : 'Personal Biodata',
        'type' : 'CV and Blogging',
        'robots' : "index, follow"           
    }     
    return site_info

def header_menu(request):
    from django.urls import reverse   
    menu_items = {}     
    item = {
        'Resume': reverse('bio:cv', kwargs={'looking':request.session['looking_for']}),
        'Senses': reverse('sense:sense_list'),
        
        
    }
    if request.user.is_superuser:
        item.update({'JobFeed': reverse('jobfeed:home')})
        item.update({'Literature': reverse('literature:home')})
        
    menu_items.update(item)
    
    return menu_items   
    


def common_process(request):
    
    lookings = dict(settings.LOOKING)
    looking = request.session['looking_for']
    alternat_looking = [l for l in lookings if l != looking and l != ''][0] 
    segments = list(filter(None, request.path.split('/')))  
    
    
    text = {
        'user_congrets': f"Hi , {request.user.username}",        
    }
    return {   
            'site': site_info(),
            'text': text, 
            'alternat_looking' : alternat_looking,   
            'header_menu' : header_menu(request),
            'segments' : segments,                   
        }
    