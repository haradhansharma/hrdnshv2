from . import views
from django.urls import path


app_name = 'sense'
urlpatterns = [ 
    path('senses/', views.post_list, name='sense_list'),
    path('senses/<str:slug>', views.post_detail, name='sense_detail'),
    path('senses/tag/<str:slug>', views.post_list, name='sense_tag'),       
]
