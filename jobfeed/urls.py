from . import views
from django.urls import path


app_name = 'jobfeed'
urlpatterns = [ 
    path('', views.home, name='home'),  
    
]