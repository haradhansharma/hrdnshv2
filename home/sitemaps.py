from django.contrib import sitemaps
from django.urls import reverse
from .models import *
from bio.models import *
from common.models import *
from home.models import *
from sense.models import *
from taggit.models import Tag
from django.conf import settings

def get_looking(arg):
    setting = settings.LOOKING[arg]
    return setting[0]

class CVSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [reverse('bio:cv', args=[str(get_looking(1))]),reverse('bio:cv', args=[str(get_looking(2))])]         
        
    def location(self, item):
        return item
    


class MySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:home','sense:sense_list', ] 
        
        
    def location(self, item):
        return reverse(item)      
    
class LookingSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [reverse('home:looking', args=[str(get_looking(1))]),reverse('home:looking', args=[str(get_looking(2))])]         
        
    def location(self, item):
        return item
    
class FirstLookCatSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8  

    def items(self):
        return ServiceCategory.objects.all().order_by('-created')[:10]
    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
        first_look = get_looking(1)        
        return "/%s/category/%s"  % (first_look, obj.slug)
    
class SecondLookCatSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8    

    def items(self):
        return ServiceCategory.objects.all().order_by('-created')[:10]
    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
        first_look = get_looking(2)     
        return "/%s/category/%s"  % (first_look, obj.slug)
    
class FirstLookServiceDetails(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8  
    
    first_look = get_looking(1)  

    def items(self):
        return MyService.objects.filter(me__me_for = self.first_look).order_by('-created')[:10]
    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
              
        return "/%s/service/%s"  % (self.first_look, obj.slug)
    
class SecondLookServiceDetails(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8    
    first_look = get_looking(2)     
    

    def items(self):
        return MyService.objects.filter(me__me_for = self.first_look).order_by('-created')[:10]

    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
        return "/%s/service/%s"  % (self.first_look, obj.slug)
    
class FirstLookWorkDetails(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8  
    
    first_look = get_looking(1)  

    def items(self):
        return MyWorks.objects.filter(me__me_for = self.first_look).order_by('-created')[:10]
    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
              
        return "/%s/works/%s"  % (self.first_look, obj.slug)
    
class SecondLookWorkDetails(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.8    
    first_look = get_looking(2)     
    

    def items(self):
        return MyWorks.objects.filter(me__me_for = self.first_look).order_by('-created')[:10]

    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
        return "/%s/works/%s"  % (self.first_look, obj.slug)   

    
class SensesDetailsSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8    

    def items(self):
        return SensePost.published.all().order_by('-updated')[:10]
    
    def lastmod(self, obj):
        return obj.created
        
    def location(self, obj):
        return reverse('sense:sense_detail', args=[str(obj.slug)])
    
class SensesTagSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8    

    def items(self):
        return Tag.objects.all().order_by('id')[:10]

        
    def location(self, obj):
        return reverse('sense:sense_tag', args=[str(obj.slug)])
    

               
    