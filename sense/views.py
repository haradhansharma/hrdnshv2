

from pprint import pprint
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from sense.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from blog.forms import CommentForm, BlogForm
from taggit.models import Tag
from django.db.models import Count, Q 
from common.common_processor import site_info, common_process
from django.template.defaultfilters import striptags





import requests

def post_list(request, slug=None):
    
 
    context = {}    
    
    query = request.GET.get('q')
    request.session['q'] = ''
    
    posts = SensePost.published.all().order_by('-updated') 
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    tag = None
    if slug:
        tag = get_object_or_404(Tag, slug=slug)
        posts=posts.filter(tags__in=[tag]).order_by('-updated')   
            
    elif query:
        request.session['q'] = query
        posts = posts.filter(Q(title__icontains=query) | Q(tags__name__icontains=query) | Q(body__icontains=query)).order_by('-updated').distinct() 
        
    else:
        posts = posts   
        
    paginator = Paginator(posts, 10)
    page = request.GET.get('page') 
    
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  
    
    tags = Tag.objects.all()    
    
    if tag:
        taged_text = f'and tagged with {tag.name}'
    else:
        taged_text = ''
    
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(reverse('sense:sense_list')),        
        'slogan' : f'List of all my senses that can be usefull to you {taged_text}!',
        'description' : f"Here's what I've been able to articulate. This list will continue to grow as long as I live. The purpose is to help you.",
        'topic' : f'Blogging',
        'type' : f'Blog',
        'robots' : f'index, follow',
        'tag' : f'Blog, blogging, sense, python, django, web development, fashion designing, technicale fahion, clo3D, apparel sourcing'
    }    
    seo_info.update(modify)   
    
    
    context['posts'] = posts
    context['pages'] = page    
    context['tag'] = tag   
    context['tags'] = tags   
    context['site'] = seo_info      
    return render(request, 'sense/senses.html', context)

def post_detail(request, slug):  
    
    request.session['q'] = ''
    
    query = request.GET.get('q')
    
    if query:
        request.session['q'] = query
        return HttpResponseRedirect(reverse('sense:sense_list') + '?q=' + query)
       
    post = get_object_or_404(SensePost, slug=slug, status='published')
    post.view += 1
    post.save()
    
    post_tags_id = post.tags.values_list('id', flat=True)
    similar_senses = SensePost.published.filter(tags__in = post_tags_id).exclude(id=post.id)
    similar_senses = similar_senses.annotate(same_tags = Count('tags')).order_by('-same_tags', '-publish')[:6] 
    tags = Tag.objects.all()    
    
    tag_list = str([tag.name for tag in post.tags.all()]).replace('[', '').replace(']', '')
    seo_info = site_info() 
    modify = {
        'canonical' : request.build_absolute_uri(reverse('sense:sense_detail', args=[str(slug)])),        
        'slogan' : f'{post.title[:80]}...',
        'description' : f"{striptags(post.body)[:160]}...",
        'topic' : f'{tag_list}',
        'type' : f'Blog',
        'robots' : f'index, follow',
        'tag' : f'Blog, blogging, sense, python, django, web development, fashion designing, technicale fahion, clo3D, apparel sourcing',
        'og_image' : post.image.url if post.image else seo_info['og_image']
        
    }    
    seo_info.update(modify)   
    
    
    context = {
        'post':post,
        'tags' : tags,
        'similar_senses':similar_senses,
        'site' : seo_info    
    }             
    
    return render(request, 'sense/post_detail.html', context = context)