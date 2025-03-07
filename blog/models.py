from django.db import models


class Tag(models.Model):
    """Represents a tag for categorizing blog posts."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """ Represents an author of a blog post. """
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """ Represents a blog post. """
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="blog_posts")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ String representation of a BlogPost instance. """
        return self.title
