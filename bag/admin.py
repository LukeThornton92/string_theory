from django.contrib import admin
from blog.models import BlogPost, Author


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'title',
        'content',
        'tags'
    )
    list_filter = (
        'created_at',
        'author', 'tags'
    )
    date_hierarchy = 'created_at'


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
    search_fields = (
        'name',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author, AuthorAdmin)
