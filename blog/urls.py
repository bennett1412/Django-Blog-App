from django.urls import path
from .views import (
    PostListView, 
    homeView,
    aboutView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>/',UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('about/',aboutView, name = 'blog-about')
    
]