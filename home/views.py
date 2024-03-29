from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from bio.helper import get_me_data
from .decorators import looking_for_required, no_looking_required, set_looking_for
from common.common_processor import site_info, common_process
from django.template.defaultfilters import striptags
from common.common_processor import looking_list
from django.contrib import messages


def home(request):  
    looking_for = request.session.get('looking_for')
    
    redirect = HttpResponseRedirect(reverse('home:looking', kwargs={'looking': str(looking_for)}))             
    if request.session['looking_for'] not in looking_list():            
        pass
    else:
        return redirect   
    
    
         
    form = LookingForm()  
    if request.method == 'POST':
        form = LookingForm(request.POST)  
        if form.is_valid():
            looking = form.cleaned_data['looking_for']     
            if looking:                 
                request.session['looking_for'] = looking            
                return  HttpResponseRedirect(reverse('home:looking', kwargs={'looking': str(looking)}))
            else: 
                context = {                    
                    'form' : form     
                    }
                return render(request, 'home/index.html', context = context)
    context = {        
        'form' : form     
        }
    return render(request, 'home/index.html', context = context)

@set_looking_for
@looking_for_required
def looking(request, **kwargs): 
    looking = kwargs['looking']
    
    # if looking == 'None':
    #     messages.warning(request,f'Please choose the area from below...')            
    #     return HttpResponseRedirect('/')
     
    me_data = get_me_data(request)     
        
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(request.path),        
        'slogan' : f'Overview about me related to {looking} sector',
        'description' : f'{striptags(me_data.summary)[:160]}...',
        'topic' : f'{looking} overview ',
        'type' : f'My Overview',
        'robots' : f'index, follow',
        'og_image' : me_data.photo.url 
    }    
    seo_info.update(modify)   
    
    context = {
        'me_data': me_data,
        'alter' : reverse('home:looking', args=[str(common_process(request).get('alternat_looking'))]) ,
        'site' : seo_info,
    }
    return render(request, 'home/looking.html', context = context)

