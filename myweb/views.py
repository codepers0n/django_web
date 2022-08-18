import http
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)



def portfolio(request):
    return render(request, 'blog/portfolio.html')