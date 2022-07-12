from django.shortcuts import render

def view_cat(request, slug):
    context = {
        'me_data': 'me_data'      
    }
    return render(request, 'bio/category.html', context = context)

def service_details(request, slug):
    
    context = {
        'me_data': 'me_data'      
    }
    return render(request, 'bio/category.html', context = context)
    
