from django.conf import settings
from django.db import models

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
    
class MySkills(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE, related_name='myskills')
    cat_of_skill = models.CharField(max_length=252)
    skill_in = models.TextField()
    
    
    def __str__(self):
        return str(self.cat_of_skill) + ' for ' + str(self.me)