from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('add/', views.add_blog_post, name='add_blog'),
]