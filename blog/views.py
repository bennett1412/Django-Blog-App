from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.

def homeView(request):
    context = {
        "posts": post.objects.all()
    }
    return render(request,'blog/home.html',context)

def aboutView(request):
    return render(request, 'blog/about.html',{})    