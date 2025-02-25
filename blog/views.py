from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogPostForm
from. models import BlogPost, Author, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def all_blog_posts(request):
    """A view to return the blog page, using pagination to show 3 blogs per page"""
    # Show 3 posts per page, defaults to page 1.
    default_page = 1
    page = request.GET.get('page', default_page)
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    tags = Tag.objects.all()
    paginator = Paginator(blog_posts, 3)  # 3 posts per page

    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(default_page)  # If page is not an integer, show the first page
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)  # If page is out of range, show last page

    return render(request, 'blog/blog.html', {'blog_page': blog_page, 'tags': tags})

def blog_detail(request, blog_id):
    """A view to display a single blog post."""
    post = get_object_or_404(BlogPost, id=blog_id)
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

def blog_list_by_tag(request, tag_id):
    default_page = 1
    page = request.GET.get('page', default_page)
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    tag = get_object_or_404(Tag, id=tag_id)
    blog_posts = BlogPost.objects.filter(tags=tag)
    paginator = Paginator(blog_posts, 3)

    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(default_page)  # If page is not an integer, show the first page
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)  # If page is out of range, show last page

    return render(request, 'blog/blog_list.html', {
        'blog_page': blog_page,
        'tag': tag
    })

@login_required
def delete_blog(request, blog_id):
    """ Deletes a Blog from the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners and authors are allowed to do that!')
        return redirect(reverse('home'))
    
    blog = get_object_or_404(BlogPost, pk = blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))

@login_required
def edit_blog(request, blog_id):
    """ Edit a Blog from the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners and authors are allowed to do that!')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, pk = blog_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited blog!')
            return redirect(reverse('product_detail', args = [blog.id]))
        else:
            messages.error(request, 'Failed to edit product, please ensure for is valid')
    else:
        form = BlogPostForm(instance = blog)
        messages.info(request, f'You are editing {blog.title} originally written by {blog.author}')

    template = 'blog/edit_blog.html'
    context = {
        'form' : form,
        'blog' : blog,
    }

    return render(request, template, context)