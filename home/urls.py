from . import views
from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('at/<str:looking>/', views.looking, name='looking'),
    path('elsifightbuilder/', TemplateView.as_view(template_name="home/elsifight.html"), name='elsifightbuilder'),
    
    
]

# hx_urlpatterns = [
    
#     path('check_type_to_get_expert/', views.check_type_to_get_expert, name='check_type_to_get_expert'),
#     path('dashboard/add_extra/<str:pk>', views.add_extra, name='add_extra'),
#     path('dashboard/sub_extra/<str:pk>', views.sub_extra, name='sub_extra'),
    
# ]

# urlpatterns += hx_urlpatterns