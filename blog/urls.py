from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog_post, name='add_blog'),
    path(
        'blog/tag/<int:tag_id>/',
        views.blog_list_by_tag,
        name='blog_list_by_tag',
        ),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]