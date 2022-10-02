from . import views
from django.urls import path






app_name = 'bio'
urlpatterns = [
 
    path('<str:looking>/category/<str:slug>', views.view_cat, name='view_cat'),
    path('<str:looking>/service/<str:slug>', views.service_details, name='service_details'),
    path('<str:looking>/works/<str:slug>', views.work_details, name='work_details'),
    path('cv/<str:looking>', views.cv, name='cv'),    
    path('cv/<str:looking>/pdf', views.cvpdf, name='cvpdf'),
 
    
   
    
    
    
]
