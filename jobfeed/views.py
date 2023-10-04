from pprint import pprint
import time
import datetime
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import feedparser

@login_required
def home(request):
    if not request.user.is_superuser:
        raise Http404
    
    template_name = 'jobfeed/home.html'   
    
    # RSS feed URL
    rss_url = "https://www.upwork.com/ab/feed/jobs/rss?sort=recency&or_terms=web+development%2C+web+programming%2C+backend+development%2C+Django%2C+RestAPI%2C++API%2C+RESTful%2C+opencart%2C+python%2C+website%2C+back+end%2C+Full+stack%2C+Fullstack&exclude_terms=figma%2C+UI%2C+UX&paging=0%3B50&api_params=1&q=NOT+%28figma+OR+UI+OR+UX%29+AND+%28web+OR+development+OR+web+OR+programming+OR+backend+OR+development+OR+Django+OR+RestAPI+OR+API+OR+RESTful+OR+opencart+OR+python+OR+website+OR+back+OR+end+OR+Full+OR+stack+OR+Fullstack%29&securityToken=69fc59f3d6e8619bf1c37347095eafd33d9f42867ec7bb671fdb1f8d7228abd4c1c7c70f0ae10e6497db35604e3a19d2fd6c57cff5ecd3945bed56c4da440477&userUid=1335236410615816192&orgUid=1335236410624204801"

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    
  

    data = []

    # Extract and print information for each item in the feed
    for item in feed.entries:      
        data.append({
            'title' : item.title,
            'link' : item.link,
            'summary' : ' '.join(item.summary.replace('\n\n', '').split()),
            'published' : item.published,
            'published_parsed' : datetime.datetime.fromtimestamp(time.mktime(item.published_parsed)) ,   
            
        })
        

    context = {
        'data' : data        
    }
    
    return render(request, template_name, context=context)
    