from . import views
from django.urls import path


app_name = 'bio'
urlpatterns = [
    
    path('category/<str:slug>', views.view_cat, name='view_cat'),
    path('service/<str:slug>', views.service_details, name='service_details'),
    
    
]
