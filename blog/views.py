from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def all_blog_posts(request):
    """A view to return the blog page"""
    return render(request, 'blog/blog.html')

def add_blog_post(request):
    """A view to return the blog page"""
    return render(request, 'blog/add_blog.html')


