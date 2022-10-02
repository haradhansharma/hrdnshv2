

from pprint import pprint
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from sense.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from blog.forms import CommentForm, BlogForm
from taggit.models import Tag
from django.db.models import Count, Q 



import requests

def post_list(request, slug=None):
    
 
    context = {}    
    posts = SensePost.published.all()#using custom manager    
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    tag = None
    if slug:
        tag = get_object_or_404(Tag, slug=slug)
        posts=posts.filter(tags__in=[tag])    
            
    query = request.GET.get("q")      
    if query:
        posts=SensePost.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
    
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  
    
    tags = Tag.objects.all()    
    context['posts'] = posts
    context['pages'] = page    
    context['tag'] = tag   
    context['tags'] = tags      
    return render(request, 'sense/senses.html', context)

def post_detail(request, slug):  
       
    post = get_object_or_404(SensePost, slug=slug, status='published')
    post.view += 1
    post.save()
    
    post_tags_id = post.tags.values_list('id', flat=True)
    similar_senses = SensePost.published.filter(tags__in = post_tags_id).exclude(id=post.id)
    similar_senses = similar_senses.annotate(same_tags = Count('tags')).order_by('-same_tags', '-publish')[:6] 
    tags = Tag.objects.all()    
    context = {
        'post':post,
        'tags' : tags,
        'similar_senses':similar_senses        
    }             
    
    return render(request, 'sense/post_detail.html', context = context)