from . import views
from django.urls import path


app_name = 'common'
urlpatterns = [   
   
    path('webmanifest/', views.webmanifest, name='webmanifest'),
    
]
