# Funtion protector to access by reprot creator only.
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.contrib import messages
from common.common_processor import looking_list

def set_looking_for(function):
    
    def wrap(request, *args, **kwargs):
        if kwargs.get('looking'):
            request.session['looking_for'] = kwargs['looking']           
            return function(request, *args, **kwargs)
        else:
            messages.warning(request,'Choose the area in which you need help from the box below!')       
            return HttpResponseRedirect(reverse('home:home'))  
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__                
    return wrap
            
            


def looking_for_required(function):    
    def wrap(request, *args, **kwargs):       
        if request.session['looking_for'] not in looking_list():     
            messages.warning(request,'Choose the area in which you need help from the box below!')       
            return HttpResponseRedirect(reverse('home:home'))            
        else:
            request.session['looking_for'] = kwargs['looking']
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__                
    return wrap

def no_looking_required(function):     
    def wrap(request, *args, **kwargs):       
        # next = request.META.get('HTTP_REFERER', None) 
        
        # if next:
        #     redirect = HttpResponseRedirect(next)
        # else:
        redirect = HttpResponseRedirect(reverse('home:looking', kwargs={'looking': str(request.session['looking_for'])})) 
            
        if request.session['looking_for'] not in looking_list():            
            return function(request, *args, **kwargs)         
        else:
            return redirect            
            
            
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__                
    return wrap