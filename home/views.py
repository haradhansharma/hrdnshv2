from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from bio.helper import get_me_data
from .decorators import looking_for_required, no_looking_required



@no_looking_required
def home(request):   
    print('from home______________________')
    print(request.session.items())  
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
    
    me_data = get_me_data(request)
    
    
    context = {
        'me_data': me_data      
    }
    return render(request, 'home/looking.html', context = context)

