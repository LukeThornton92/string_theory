from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm
from. models import BlogPost

# Create your views here.

def all_blog_posts(request):
    """A view to return the blog page"""
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})

def blog_detail(request, id):
    """A view to display a single blog post."""
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def add_blog_post(request):
    """A view to add a blog to the blog page"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authenticated authors are allowed to add to the blog!')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog successfully added!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add blog, please ensure form is valid')
    else:
        form = BlogPostForm(user=request.user)

    template = 'blog/add_blog.html'
    context = {
        'form' : form
    }
    return render(request, template, context)
