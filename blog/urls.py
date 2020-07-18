from django.urls import path
from .views import (
    homeView,
    aboutView,
)

app_name = 'blog'

urlpatterns = [
    path('',homeView, name = 'blog-home'),
    path('about/',aboutView, name = 'blog-about')
]