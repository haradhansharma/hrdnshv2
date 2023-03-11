from django.contrib import messages
from django.test import override_settings
import pdfkit
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from bio.helper import get_me_data
from home.decorators import looking_for_required, no_looking_required, set_looking_for
from .models import *
from common.common_processor import site_info, common_process
import platform
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.defaultfilters import striptags
from django.conf import settings
# helper function 


def get_verbose_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()


@set_looking_for
@looking_for_required
def view_cat(request, **kwargs): 
    
    slug = kwargs['slug']
    looking = kwargs['looking']
    me_data = get_me_data(request)
    
    category = ServiceCategory.objects.get(slug=slug)
    me = Me.objects.get(me_for=looking)
    services = category.services.filter(me=me)
    
    
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(reverse('bio:view_cat', args=[str(looking), slug])),        
        'slogan' : f'categorywise service for category {category.name}',
        'description' : f'{striptags(me_data.summary)[:160]}...',
        'topic' : f'Category wise service list that I provide',
        'type' : f'Service List',
        'robots' : f'index, follow'
    }    
    seo_info.update(modify)     

    categoris_of_products = set()
    related_service_by_categories = set()
    for s in services:
        for c in s.category.all():
            if c != category:
                categoris_of_products.add(c)
                for ser in c.services.filter(me=me):
                    related_service_by_categories.add(ser)
    rsbc = [s for s in related_service_by_categories if s not in services]
    context = {
        'services': services,
        'me_data': me_data,
        'category': category,
        'categoris_of_products': list(categoris_of_products),
        'related_service_by_categories': rsbc,
        'site' : seo_info,
        'alter' : reverse('bio:view_cat', args=[str(common_process(request).get('alternat_looking')), slug]) 
        
    }
    return render(request, 'bio/category.html', context=context)


def comparision(service):
    com_data = {}   
    ex_labels = ExtraLabel.objects.filter(l_for = service.me )
    title = []
    description = []
    delivery_time = []
    revision = []
    price = []
    extra = []
    
    for service_option in service.myservice.all():        
        for field in service_option._meta.fields:
            if field.name == 'title':
                title.append(getattr(service_option, field.name, None))
            if field.name == 'description':
                description.append(getattr(service_option, field.name, None))
            if field.name == 'delivery_time':
                delivery_time.append(getattr(service_option, field.name, None))
            if field.name == 'revision':
                revision.append(getattr(service_option, field.name, None))
            if field.name == 'price':
                price.append(getattr(service_option, field.name, None))
       
        el_value = {}  
        for el in service_option.get_extra:
            # value = [soe.value for soe in service_option.get_extra if el.name == soe.label.name] or ['-']
            d = {
                el.label.name : el.value if el.value else '-'
            }            
            el_value.update(d)        
        extra.append(el_value)
    if title:        
        com_data.update({get_verbose_name(service_option, 'title'):title})
    if description:
        com_data.update({get_verbose_name(service_option, 'description'):description})
    if delivery_time:
        com_data.update({get_verbose_name(service_option, 'delivery_time'):delivery_time})
    if revision:
        com_data.update({get_verbose_name(service_option, 'revision'):revision})
    if price:
        com_data.update({get_verbose_name(service_option, 'price'):price})
    
    result = compile(extra)
    for k, v in result.items():
        com_data.update({k:v})   
    
    return com_data

def compile(ls):
    dx = dict()
    for d in ls:
        for k, v in d.items():
            current = dx.get(k, [])  
            current.append(v)
            dx[k] = current
    return dx

@set_looking_for
@looking_for_required
def service_details(request, **kwargs):
    slug = kwargs['slug']
    looking = kwargs['looking']
    service = get_object_or_404(MyService, slug=slug)
    com_data = comparision(service)

    me_data = get_me_data(request)
    
    
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(reverse('bio:service_details', args=[str(looking), slug])),        
        'slogan' : f'Service details of {service.name}',
        'description' : f'{striptags(service.description)[:160]}...',
        'topic' : f'Details about service {service.name}',
        'type' : f'Details of service',
        'robots' : f'index, follow',
        'og_image' : service.get_image.picture.url
    }    
    seo_info.update(modify)   
    
    
    
    context = {
        'me_data': me_data,
        'service': service,
        'com_data': com_data,
        'site' : seo_info,
    }
    return render(request, 'bio/service_detail.html', context=context)


@set_looking_for
@looking_for_required
def work_details(request, **kwargs):
    slug = kwargs['slug']
    looking = kwargs['looking']
    me_data = get_me_data(request)
    work = get_object_or_404(MyWorks, slug=slug)
    
    
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(reverse('bio:work_details', args=[str(looking), slug])),        
        'slogan' : f'Work details of {work.title}',
        'description' : f'{striptags(work.description)[:160]}...',
        'topic' : f'Details about my work {work.title}',
        'type' : f'Details of work',
        'robots' : f'index, follow',
        'og_image' : work.get_image.picture.url if work.get_image else None
    }    
    seo_info.update(modify)   

    context = {
        'me_data': me_data,
        'service': work,
        'site' : seo_info,

    }
    return render(request, 'bio/work_detail.html', context=context)


@set_looking_for
@looking_for_required
def cv(request, **kwargs):

    looking = kwargs['looking']

 
    me_data = get_me_data(request)
    
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(request.path),        
        'slogan' : f'My HTML CV of {looking} sector',
        'description' : f'{striptags(me_data.summary)[:160]}...',
        'topic' : f'{looking} HTML CV ',
        'type' : f'Html CV',
        'robots' : f'index, follow',
        'og_image' : me_data.photo.url 
    }    
    seo_info.update(modify)   
    

    context = {
        'me_data': me_data,
        'interest' : Interest.objects.all(),
        'languge' : Languge.objects.all(),
        'alter' : reverse('bio:cv', args=[str(common_process(request).get('alternat_looking'))]),
        'site' : seo_info,


    }
    return render(request, 'bio/cv.html', context=context)

    

def render_html(request, **kwargs):
    
    me_data = get_me_data(request)    
    #active below for windows development server
    static_url = '%s://%s%s' % (request.scheme,
                                request.get_host(), settings.STATIC_URL)
    # media_url = '%s://%s%s' % (request.scheme,
    #                            request.get_host(), settings.MEDIA_URL)
    # media_link = '%s://%s%s%s' % (request.scheme,
    #                            request.get_host(), settings.STATIC_URL, settings.MEDIA_URL)
    # print(media_link)
    title = '{}_{}_cv.pdf'.format(str(((me_data.title).lower()).replace(' ', '_')), str(kwargs['looking'])) 
    
    context = {
        'me_data': me_data,
        'title' : title,
        'site' : site_info(),
        'interest' : Interest.objects.all(),
        'languge' : Languge.objects.all(),
        'education' : Education.objects.all(),        
    }
    #active below for windows development server
    with override_settings(STATIC_URL=static_url):
        template = get_template('bio/cvpdf.html')
        context = context
        html = template.render(context)
        return html

@set_looking_for
@looking_for_required
def cvpdf(request, **kwargs):
    site = site_info()
    site_email = site.get('email')
    
    
    
    content = render_html(request, **kwargs)
    
    if 'html' in request.GET:
        # Output HTML        
        return HttpResponse(content)
    else: 
        if platform.system() == 'Windows':
            wkhtmltopdf_bin = 'C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        elif platform.system() == 'Linux':
            wkhtmltopdf_bin = '/usr/local/bin/wkhtmltopdf'
        else:
            messages.warning(request,f'OS Unknow! Please drop a mail to {site_email}')    
            return  HttpResponseRedirect(reverse('home:home'))
            
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)
        options = {
            'page-size': 'A4',
            'encoding': 'UTF-8',
            'margin-top': '0.05in',
            'margin-right': '0.05in',
            'margin-bottom': '0.05in',
            'margin-left': '0.05in',            
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 1,
        }        
        pdf = pdfkit.from_string(input=content, output_path=False,
                                options=options, configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        if 'download' in request.GET and 'inline' not in request.GET:
                response['Content-Disposition'] = 'attachment; filename=%s' % '{}_{}_cv.pdf'.format(str(((get_me_data(request).title).lower()).replace(' ', '_')), str(kwargs['looking']))                
        
        return response


