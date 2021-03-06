from django.conf import settings


def site_info():
    from common.models import ExSite   
       
    site = ExSite.on_site.get()   
    site_info = {
        'name' : site.site.name,
        'domain' : site.site.domain, 
        'canonical' : site.site.domain,
        'meta_name': site.site_meta,
        'description': site.site_description,
        'tag': list((site.site_meta_tag).split(",")),
        'favicon': site.site_favicon.url,
        'mask_icon': site.mask_icon.url,
        'logo': site.site_logo.url,
        'slogan': site.slogan,
        'og_image': site.og_image.url,
        'phone': site.phone,
        'email': site.email,
        'location': site.location,
        'facebook_link': site.facebook_link,
        'twitter_link': site.twitter_link, 
        'linkedin_link': site.linkedin_link,    
           
    } 
    
    return site_info

    
    


def common_process(request):
    lookings = dict(settings.LOOKING)
    looking = request.session['looking_for']
    alternat_looking = [l for l in lookings if l != looking and l != ''][0] 
     
    
    
    text = {
        'user_congrets': f"Hi , {request.user.username}",        
    }
    return {   
            'site': site_info(),
            'text': text, 
            'alternat_looking' : alternat_looking,            
    }
    