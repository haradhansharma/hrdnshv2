from .models import *

def get_me_data(request):
    looking_session = request.session['looking_for']    
    
    if looking_session == 'web':
        me_data = Me.webobjects.get()        
    elif looking_session == 'fashion':
        me_data = Me.fashionobjects.get()
        
    return me_data
    