from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.urls import reverse
from common.common_processor import site_info, common_process
from django.templatetags.static import static





def webmanifest(request):
    site = site_info()   
    icons = []    
    ic192 = {
        "src": static(site.get('og_image')),
        "sizes": "192x192",
        "type": "image/png"        
    }
    
    icons.append(ic192)   
    ic512 = {
        "src": static(site.get('og_image')),
        "sizes": "512x512",
        "type": "image/png"        
    }
    icons.append(ic512)    
    manifest_data = {
        'name' : site.get('name') + '--' + site.get('slogan'),
        'short_name' : site.get('name'),
        'icons' : icons,
        'start_url' : site.get('domain'),
        "scope": "/",
        'lang' : 'en',
        'screenshots' : [static(site.get('og_image')), static(site.get('logo'))],
        'categories': site.get('tag'),
        
        "description": site.get('description'),
        
        "orientation": "any",
        "theme_color": "#892d2c",
        "background_color": "#892d2c",
        "display": "standalone"        
    }
    
    return JsonResponse(manifest_data, safe=False)