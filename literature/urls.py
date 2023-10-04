from . import views
from django.urls import path


app_name = 'literature'
urlpatterns = [ 
    path('home/', views.home, name='home'),  
    path('delete-idea/<int:pk>', views.delete_idea, name='delete_idea'),       
    path('configure_raw_story/<int:pk>/', views.generate_story_title_and_outline, name='generate_story_title_and_outline'),
    path('story_outline/<int:pk>/', views.story_outline, name='story_outline'),
    path('story/<int:pk>/', views.story, name='story')
]