from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.urls import reverse
from common.common_processor import site_info, common_process





def webmanifest(request):
    site = site_info()   
    icons = []    
    ic192 = {
        "src": site.get('og_image'),
        "sizes": "192x192",
        "type": "image/png"        
    }
    
    icons.append(ic192)   
    ic512 = {
        "src": site.get('og_image'),
        "sizes": "512x512",
        "type": "image/png"        
    }
    icons.append(ic512)    
    manifest_data = {
        'name' : site.get('name'),
        'short_name' : 'Haradhan Sharma',
        'icons' : icons,
        'start_url' : site.get('domain'),
        "scope": "/",
        'lang' : 'en',
        'screenshots' : [site.get('og_image'), site.get('logo')],
        'categories': site.get('tag'),
        
        'description': site.get('site_description'),      
        
        
        "theme_color": "#ffffff",
        "background_color": "#ffffff",
        "display": "standalone"        
    }
    
    return JsonResponse(manifest_data, safe=False)