from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from bio.helper import get_me_data
from .decorators import looking_for_required, no_looking_required
from common.common_processor import site_info, common_process




@no_looking_required
def home(request):       
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

@looking_for_required
def looking(request, **kwargs): 
    try:   
        me_data = get_me_data(request)  
    except:
        me_data = None
    
    context = {
        'me_data': me_data,
        'alter' : reverse('home:looking', args=[str(common_process(request).get('alternat_looking'))]) 
    }
    return render(request, 'home/looking.html', context = context)

