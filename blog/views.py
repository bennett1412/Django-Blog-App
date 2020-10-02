from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django import forms    
from .models import post
from .forms import PostCreateForm
# Create your views here.

def homeView(request):
    context = {
        "posts": post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model =  post 
    template_name = 'blog/home.html'
    context_object_name = "posts"
    ordering = ["-pub_date"]
    paginate_by = 4

class UserPostListView(ListView):
    model =  post 
    template_name = 'blog/user_posts.html'
    context_object_name = "posts"
    ordering = ["-pub_date"]
    paginate_by = 4    

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-pub_date')

class PostDetailView(DetailView):
    model =  post   

class PostCreateView(LoginRequiredMixin,CreateView):
    model =  post
    form_class = PostCreateForm

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =  post
    form_class = PostCreateForm

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False                

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =  post 
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def aboutView(request):
    return render(request, 'blog/about.html',{})    