from . import views
from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:looking>', views.looking, name='looking'),
    
    
]

# hx_urlpatterns = [
    
#     path('check_type_to_get_expert/', views.check_type_to_get_expert, name='check_type_to_get_expert'),
#     path('dashboard/add_extra/<str:pk>', views.add_extra, name='add_extra'),
#     path('dashboard/sub_extra/<str:pk>', views.sub_extra, name='sub_extra'),
    
# ]

# urlpatterns += hx_urlpatterns