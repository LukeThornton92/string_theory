from django.shortcuts import render

# Create your views here.

def all_blog_posts(request):
    """A view to return the blog page"""
    return render(request, 'blog/blog.html')

def add_blog_post(request):
    """A view to return the blog page"""
    return render(request, 'blog/add-blog.html')