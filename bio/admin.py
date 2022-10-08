from django.contrib import admin
from .models import *

admin.site.register(Me)
admin.site.register(MyLinks)
class MySkillsAdmin(admin.ModelAdmin):
    list_display = ('cat_of_skill', 'me', )
    list_filter = ('cat_of_skill','me',)
admin.site.register(MySkills, MySkillsAdmin)
class SkillsInAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'skil_value', 'show_in_front', 'show_in_cv', 'show_in_service_details','show_in_cv_tech' ,)
    list_filter = ('show_in_front','show_in_cv','show_in_service_details','show_in_cv_tech',)
    search_fields = ('name',)
admin.site.register(SkillsIn, SkillsInAdmin)


admin.site.register(ServiceCategory)
class ExtraLabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'l_for',)
    list_filter = ('l_for',)
admin.site.register(ExtraLabel, ExtraLabelAdmin)
admin.site.register(Languge)
admin.site.register(Interest)
admin.site.register(Certificate)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'me', 'school', 'period',)
    list_filter = ('me',)
admin.site.register(Education, EducationAdmin)

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'me', 'related_work', 'period','serial', 'active')
    list_filter = ('me','related_work','active',)
admin.site.register(WorkExperience, WorkExperienceAdmin)


class ExtraOfOptions(admin.TabularInline):
    model = ExtraOfOptions
    extra = 0 
    fk_name = "option"


class ServiceOptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'price', 'delivery_time','revision',)
    list_filter = ('service',)
    inlines = [ExtraOfOptions]
    
admin.site.register(ServiceOption, ServiceOptionAdmin) 
    

    

class ServiceOption(admin.TabularInline):
    model = ServiceOption
    extra = 0 
    fk_name = "service"
    show_change_link = True
    
class ServiceImage(admin.TabularInline):
    model = ServiceImage
    extra = 0 
    fk_name = "service"

class MyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'me', 'mp_links',)
    list_filter = ('me',)
    inlines = [ServiceImage, ServiceOption]
    
admin.site.register(MyService, MyServiceAdmin) 


class WorkImage(admin.TabularInline):
    model = WorkImage
    extra = 0 
    fk_name = "work"
    
class WorkExperience(admin.TabularInline):
    model = WorkExperience
    extra = 0 
    fk_name = "related_work"

class MyWorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'me', )
    list_filter = ('me',)
    inlines = [WorkImage, WorkExperience]
    
admin.site.register(MyWorks, MyWorksAdmin) 



