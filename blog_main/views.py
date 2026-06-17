
from django.http import HttpResponse
from django.shortcuts import render

from about.models import About

from blog.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,  status = 'Published')
    posts = Blog.objects.filter(is_featured = False, status = 'Published')

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    
    return render(request, 'home.html', context)


