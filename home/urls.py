from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from .sitemaps import *
from django.contrib.sitemaps.views import sitemap


app_name = 'home'

sitemap_list = {
    'static': MySitemap,
    'cvsitemap' : CVSitemap,
    'looking': LookingSitemap,
    'firstlookcat': FirstLookCatSitemap,   
    'secondlookcat' : SecondLookCatSitemap,
    'firstlookservice' : FirstLookServiceDetails,
    'secondlookservice' : SecondLookServiceDetails,
    'firstlookworks' : FirstLookWorkDetails,
    'secondlookworks' : SecondLookWorkDetails,
    'senses': SensesDetailsSitemap,
    'sensestagsitemap' : SensesTagSitemap
    
    
    
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemap_list}, name='django.contrib.sitemaps.views.sitemap'),      
    path('', views.home, name='home'),
    path('at/<str:looking>/', views.looking, name='looking'),
    path('elsifightbuilder/', TemplateView.as_view(template_name="home/elsifight.html"), name='elsifightbuilder'),   
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robot'), 
    
]

