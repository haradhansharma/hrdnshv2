from audioop import reverse

from django.conf import settings
from django.shortcuts import redirect
from .models import *
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve, reverse



class HomeMiddleware:  
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response
        
    

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        
        """
        
      
        if 'looking_for' not in request.session:
            request.session['looking_for'] = None
            

        
        
        
        
        '''
        do not delete below line. write anything before to call before view call
        '''    
        response = self.get_response(request) 
        
        # Code to be executed for each request/response after
        # the view is called.
        return response
    
    
    
    
        
        

        