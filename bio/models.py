from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
import random
import string

from django.urls import reverse

class WebManager(models.Manager):    
    def get_queryset(self):        
        return super(WebManager, self).get_queryset().filter(me_for='web')
    
class FashionManager(models.Manager):    
    def get_queryset(self):        
        return super(FashionManager, self).get_queryset().filter(me_for='fashion')
   
    

class Me(models.Model):
    me_for = models.CharField(max_length=10, choices=settings.LOOKING, unique=True)
    title = models.CharField(max_length=252)
    summary = models.TextField()
    photo = models.ImageField(upload_to='me_photo')
    
    @property
    def get_links(self):
        return self.mylinks.all()
    
    @property
    def get_skills(self):
        return self.myskills.all()    
    
    def __str__(self) -> str:
        return self.me_for
    
    objects = models.Manager()
    webobjects = WebManager()
    fashionobjects = FashionManager()
    
class MyLinks(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='mylinks')
    links = models.URLField(blank=True,)
    text_to_show = models.CharField(max_length=252)
    icon = models.TextField()
    
    def __str__(self):
        return str(self.text_to_show) + ' for ' + str(self.me)
    
class SkillsIn(models.Model):
    name = models.CharField(max_length=252)
    link = models.URLField()
    
    def __str__(self) -> str:
        return self.name
    
    
class MySkills(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myskills')
    cat_of_skill = models.CharField(max_length=252)
    skills_in = models.ManyToManyField(SkillsIn, related_name='skillsin')
    
    
    def __str__(self):
        return str(self.cat_of_skill) + ' for ' + str(self.me)
    
class ServiceCategory(models.Model):
    name = models.CharField(max_length=252)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.name)
            while self.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.name + ' ' + random_string)
            self.slug = slug_sample
        super(ServiceCategory, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    @property
    def number_of_service(self):
        return MyService.objects.filter(category=self).count()
    
    @property
    def services(self):
        return MyService.objects.filter(category=self)
    
    def get_absolute_url(self):
        return reverse('bio:view_cat', kwargs={'slug': self.slug})
    
class ServiceOption(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color_hex = models.CharField(max_length=7)
    price = models.DecimalField(decimal_places=2,max_digits=2)
    delivery_time = models.CharField(max_length=5)
    revision = models.IntegerField()
    
    def __str__(self):
        return self.title



class MyService(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myservice')
    slug = models.SlugField()
    name = models.CharField(max_length=252)
    picture = models.ImageField(upload_to = 'service_image')
    description = models.TextField()
    category = models.ManyToManyField(ServiceCategory, related_name='categories')
    service_option = models.ManyToManyField(ServiceOption, related_name='options')
    mp_links = models.TextField()# need take help of custom tag, name=link patern should follow to write
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.name)
            while self.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.name + ' ' + random_string)
            self.slug = slug_sample
        super(MyService, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bio:service_details', kwargs={'slug': self.slug})
    