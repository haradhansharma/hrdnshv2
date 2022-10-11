from email.policy import default
from urllib.parse import urlparse, urlunparse
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
    def get_cv_links(self):
        links = self.mylinks.filter(to_cv=True)
        
        link_list = []
        for l in links:
            link_list.append({urlparse(l.links).path : l.icon})        
        return link_list
    
    @property
    def get_skills(self):
        return self.myskills.all()    
    
    @property
    def get_cvskillsIn(self):
        skills = self.myskills.all()    
        skill_list = {}
        for s in skills:
            for sk in s.cv_skills_in:
                skill_list.update({sk.name : sk.skil_value})        
        return skill_list  
    
    @property
    def get_services(self):
        return self.myservice.all()    
    
    @property
    def get_works(self):
        return self.myworks.all()  
    
    @property
    def get_education(self):
        return self.myeducation.all()
    
    @property
    def work_experience(self):
        return self.workexperience.filter(active = True).order_by('serial')
    
    @property
    def get_certificate(self):
        return self.certificate.all()

    
    def __str__(self) -> str:
        return self.me_for
    
    objects = models.Manager()
    webobjects = WebManager()
    fashionobjects = FashionManager()
    
class Certificate(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='certificate')
    name = models.CharField(max_length=252)
    digital_pic = models.ImageField(upload_to='certificate')
    valid_link = models.URLField()
    
    
    def __str__(self):
        return self.name
    
    
class Languge(models.Model):    
    name = models.CharField(max_length=252)
    type = models.CharField(max_length=252)    
    def __str__(self):
        return self.name
    
class Interest(models.Model):    
    name = models.CharField(max_length=252)   
    def __str__(self):
        return self.name
    
class Education(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myeducation')
    title = models.CharField(max_length=252)
    school = models.CharField(max_length=252, null=True, blank=True)
    period = models.CharField(max_length=252, null=True, blank=True)

    def __str__(self):
        return self.title
    
class MyLinks(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='mylinks')
    links = models.URLField(blank=True,)
    text_to_show = models.CharField(max_length=252)
    icon = models.TextField()
    to_cv = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.text_to_show) + ' for ' + str(self.me)
    
class SkillsIn(models.Model):
    name = models.CharField(max_length=252)
    link = models.CharField(blank=True, null=True, max_length=252)
    skil_value = models.IntegerField(default=0)
    show_in_front = models.BooleanField(default=True)
    show_in_cv = models.BooleanField(default=True)
    show_in_service_details = models.BooleanField(default=True)
    show_in_work_details = models.BooleanField(default=True)
    show_in_cv_tech = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return str(self.name) + '-' + str(self.skil_value)
    
    
class MySkills(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myskills')
    cat_of_skill = models.CharField(max_length=252)
    skills_in = models.ManyToManyField(SkillsIn, related_name='skillsin')
    
    @property
    def front_skills_in(self):
        data = self.skills_in.filter(show_in_front=True)
        return data
    @property
    def cv_skills_in(self):
        data = self.skills_in.filter(show_in_cv = True)
        return data
    @property
    def service_details_skills_in(self):
        data = self.skills_in.filter(show_in_service_details = True)
        return data
    @property
    def works_details_skills_in(self):
        data = self.skills_in.filter(show_in_work_details = True)
        return data
    
    @property
    def cv_tech_skills_in(self):
        data = self.skills_in.filter(show_in_cv_tech = True)
        return set(data)
    
    
    def __str__(self):
        return str(self.cat_of_skill) + ' for ' + str(self.me)
    
class ServiceCategory(models.Model):
    name = models.CharField(max_length=252)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)    
    objects = models.Manager()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.name)            
            if ServiceCategory.objects.filter(slug=slug_sample).exists():
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


class MyService(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myservice')
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=252)    
    description = models.TextField()
    category = models.ManyToManyField(ServiceCategory, related_name='categories')    
    mp_links = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True) 
    skills_involved = models.ManyToManyField(MySkills, related_name='skillsinservice')
    
    
    dark_head_class = models.CharField(max_length=15, default='bg-deepgrey')
    dark_body_class = models.CharField(max_length=15, default='bg-lightgrey')
    dark_link_class = models.CharField(max_length=15, default='link-lightgrey')
    
    
    
    light_head_class = models.CharField(max_length=15, default='bg-darkbeige')
    light_body_class = models.CharField(max_length=15, default='bg-brightbeige')
    light_link_class = models.CharField(max_length=25, default='link-brightbeige')
    
    
    objects = models.Manager()
    
    @property
    def get_image(self):
        return self.serviceimage.filter(front=True).first()
    
    @property
    def get_images(self):
        return self.serviceimage.all()
    
    def get_starting_price(self):
        options = self.myservice.all()
        price = []
        for option in options:
            price.append(option.price)
        return min(price)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.name)
            while MyService.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.name + ' ' + random_string)
            self.slug = slug_sample
        super(MyService, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    # abandoned due to compolsurity of session so calling from template
    # def get_absolute_url(self):
    #     return reverse('bio:service_details', kwargs={'slug': self.slug})
    

    
    
class ServiceImage(models.Model):
    service = models.ForeignKey(MyService, on_delete=models.CASCADE, related_name='serviceimage')
    picture = models.ImageField(upload_to = 'service_image')
    title = models.CharField(max_length=152)
    description = models.CharField(max_length=252)
    alt = models.CharField(max_length=152)
    front = models.BooleanField(default=False)
    

    
class ServiceOption(models.Model):
    service = models.ForeignKey(MyService, on_delete=models.CASCADE, related_name='myservice')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color_hex = models.CharField(max_length=7)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    delivery_time = models.CharField(max_length=5)
    revision = models.IntegerField()
    
    @property
    def get_extra(self):
        return self.additional.all()
    
    
    def __str__(self):
        return str(self.title) + ' for ' + str(self.service.name)
    
class ExtraLabel(models.Model):
    name = models.CharField(max_length=252)
    l_for = models.CharField(max_length=10, choices=settings.LOOKING, default = 'web')
    def __str__(self):
        return self.name
    
class ExtraOfOptions(models.Model):
    option = models.ForeignKey(ServiceOption, on_delete=models.CASCADE, related_name='additional')
    label = models.ForeignKey(ExtraLabel, on_delete=models.CASCADE, related_name = 'exlabel', default=1)    
    value = models.CharField(max_length=252)
    
   

class MyWorks(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myworks')
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    short_des = models.TextField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True) 
    skills_involved = models.ManyToManyField(MySkills, related_name='skillsinworks')
    
    category = models.ManyToManyField(ServiceCategory, related_name='workcategories')    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.title)
            while MyWorks.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.title + ' ' + random_string)
            self.slug = slug_sample
        super(MyWorks, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title) + ' for ' + str(self.me)
    
    @property
    def get_image(self):
        return self.workimage.all()[0]
    
    @property
    def get_images(self):
        return self.workimage.all()
    
class WorkExperience(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='workexperience')    
    title = models.CharField(max_length=252)
    related_work = models.ForeignKey(MyWorks, on_delete=models.CASCADE, related_name='relatedwork')
    summary = models.TextField()
    achivements = models.TextField()
    period = models.CharField(max_length=252, null=True, blank=True)
    serial = models.BigIntegerField(default=0)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True) 
    
    @property
    def technology_used(self):
        skills = self.related_work.skills_involved.all()   
        skill_set = set()
        for skill in skills:
            for s in skill.cv_tech_skills_in:
                skill_set.add(s)
   
        return skill_set
    
    def __str__(self):
        return str(self.title) + ' for ' + str(self.related_work.title)

class WorkImage(models.Model):
    work = models.ForeignKey(MyWorks, on_delete=models.CASCADE, related_name='workimage')
    picture = models.ImageField(upload_to = 'work_image')
    title = models.CharField(max_length=152)
    description = models.CharField(max_length=252)
    alt = models.CharField(max_length=152)
    