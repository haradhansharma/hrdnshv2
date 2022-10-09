from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.validators import FileExtensionValidator

class ExSite(models.Model):    
    site = models.OneToOneField(Site, primary_key=True, verbose_name='site', on_delete=models.CASCADE)
    site_meta = models.CharField(max_length=256)
    site_description = models.TextField(max_length=500)
    site_meta_tag =models.CharField(max_length=255)
    site_favicon = models.ImageField(upload_to='site_image')
    site_logo = models.ImageField(upload_to='site_image')
    slogan = models.CharField(max_length=150, default='')
    og_image = models.ImageField(upload_to='site_image')
    mask_icon = models.FileField(upload_to='site_image', validators=[FileExtensionValidator(['svg'])])
    
    
    phone = models.CharField(max_length=15)
    email = models.EmailField()    
    location=models.CharField(max_length=120, null=True, blank=True)
    # facebook = models.URLField(null=True, blank=True)
    # twitter = models.URLField(null=True, blank=True)
    # linkedin = models.URLField(null=True, blank=True)   
    # github =  models.URLField(null=True, blank=True) 

    
    
    objects = models.Manager()
    on_site = CurrentSiteManager('site')
    
    def __str__(self):
        return self.site.__str__()  
