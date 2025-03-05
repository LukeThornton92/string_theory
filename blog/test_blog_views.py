from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Author, BlogPost, Tag
from django.utils import timezone
from django.contrib.messages import get_messages


class BlogViewsTest(TestCase):
    def setUp(self):
        self.super_user = User.objects.create_superuser(username='superuser', password='password')
        self.user = User.objects.create_user(username='notsuperuser', password='password2')

    def test_blog_view(self):
        """ Test to see if Blog renders page """
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_add_view_superuser(self):
        """ Test to see if Blog create page renders for logged-in superuser """
        self.client.login(username='superuser', password='password')

        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog post',
            'author': self.super_user.id,
            'tag_string': 'test, blog',
        }

        url = reverse('add_blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Ensure form fields are present
        self.assertContains(response, 'name="title"')
        self.assertContains(response, 'name="content"')
        self.assertContains(response, 'name="tag_string"')

    def test_blog_add_post_superuser(self):
        """ Test adding a blog post via POST request """
        self.client.login(username='superuser', password='password')
        url = reverse('add_blog')

                    # Create tag instances
        tag1 = Tag.objects.create(name="test")
        tag2 = Tag.objects.create(name="blog")

        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog post',
            'author': self.super_user.id,
            'tag_string': 'Test, Blog',
        }

        # Send POST request
        url = reverse('add_blog')
        response = self.client.post(url, data, follow=True)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Blog successfully added!")
        
    def test__blog_add_post_notsuperuser(self):
        """Ensures a normal user cant make blog post"""
        self.client.login(username='notsuperuser', password='password2')

        url = reverse('add_blog') 

        data = {
            "title": "Unauthorized Post",
            "content": "This should not be allowed.",
            "tag_string": "test, blog",
        }

        response = self.client.post(url, data, follow=True)

        # Check that the error message was sent
        messages = list(response.context.get("messages", []))
        self.assertTrue(any("only authenticated authors" in str(msg) for msg in messages))

        url = reverse('add_blog')

    def test_edit_blog_non_superuser_redirects(self):
        """Ensure a non-superuser cannot edit a blog post and is redirected to home."""
        author = Author.objects.create(name="John Doe")  # Creates an Author instance

        blog = BlogPost.objects.create(
            title="Test Blog",
            content="Test Content",
            author=author  # Assign the Author instance
        )

        self.client.login(username='notsuperuser', password='password2')
        
        url = reverse('edit_blog', args=[blog.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302) #redirect
        self.assertRedirects(response, reverse('home'))

    def test_edit_blog_superuser_(self):
        """Ensures a superuser can edit a blog post"""
        author = Author.objects.create(name="John Doe")  # Creates an Author instance

        blog = BlogPost.objects.create(
            title="Test Blog",
            content="Test Content",
            author=author  # Assign the Author instance
            
        )

        self.client.login(username='superuser', password='password')
        
        url = reverse('edit_blog', args=[blog.id])
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You are editing Test Blog originally written by John Doe")

        response = self.client.post(
        url,
        {
            "title": "Updated Test Blog",
            "content": "Updated content",
            "tag_string": "Updated, Tags",
            "author": author.id  # Make sure to pass the correct author reference
        },
        follow=True  # Follow redirects
        )

        # Step 3: Check the success message after editing
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully edited blog!")

    def test_superuser_delete_blog(self):
        """Ensure a superuser can delete a blog post."""
        self.author = Author.objects.create(name="John Doe")  # Ensure Author exists
        self.blog = BlogPost.objects.create(
            title="Test Blog",
            content="This is a test blog post",
            author=self.author
        )
        self.client.login(username='superuser', password='password')

        url = reverse('delete_blog', args=[self.blog.id])
        response = self.client.post(url, follow=True)  # Send a POST request

        self.assertFalse(BlogPost.objects.filter(id=self.blog.id).exists())  # Blog should be deleted

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Blog deleted!")

    def test_delete_blog_non_superuser_redirects(self):
        """Ensure a normal user cannot delete a blog post."""

        self.author = Author.objects.create(name="John Doe")
        self.blog = BlogPost.objects.create(
            title="Test Blog",
            content="This is a test blog post",
            author=self.author 
        )
        self.client.login(username='notsuperuser', password='password2')

        url = reverse('delete_blog', args=[self.blog.id])
        response = self.client.post(url, follow=True)

        self.assertTrue(BlogPost.objects.filter(id=self.blog.id).exists())  # Blog should NOT be deleted

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners and authors are allowed to do that!")

        self.assertRedirects(response, reverse('home'))
    
class BlogViewsTagTest(TestCase):
    def setUp(self):
        """Set up test data for blog posts and tags."""
        self.tag = Tag.objects.create(name="Test Tag")
        self.author = Author.objects.create(name="John Doe")

        # Creates 5 blog posts with the same tag (to test pagination)
        for i in range(5):
            blog = BlogPost.objects.create(
                title=f"Test Blog {i+1}",
                content="This is a test blog post",
                author=self.author
            )
            blog.tags.add(self.tag)  # Assign the tag to the blog post

        self.url = reverse('blog_list_by_tag', args=[self.tag.id])

    def test_blog_list_by_tag(self):
        """Ensure the correct blog posts are returned for a tag."""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertEqual(response.context['tag'], self.tag)

        blog_page = response.context['blog_page']
        self.assertEqual(blog_page.paginator.num_pages, 2)  # 5 posts, 3 per page

        # Ensure only the first 3 posts appear on the first page
        self.assertEqual(len(blog_page.object_list), 3)

    def test_blog_list_by_tag_pagination(self):
        """Test pagination for blog list by tag."""
        response = self.client.get(self.url, {'page': 2})
        self.assertEqual(response.status_code, 200)

        blog_page = response.context['blog_page']
        self.assertEqual(len(blog_page.object_list), 2)  # Only 2 posts on page 2

    def test_blog_list_by_tag_invalid_page(self):
        """Test handling of an out-of-range page number."""
        response = self.client.get(self.url, {'page': 999})
        self.assertEqual(response.status_code, 200)

        blog_page = response.context['blog_page']
        self.assertEqual(len(blog_page.object_list), 2)  # Should show last available page (2 posts)
    
class AuthorModelTest(TestCase):
    def test_create_author(self):
        """Test creating an Author instance"""
        author = Author.objects.create(name="John Doe", bio="Test bio")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.bio, "Test bio")
        self.assertIsNotNone(author.created_at)

class BlogPostModelTest(TestCase):
    def test_create_blog_post(self):
        """Test creating a BlogPost instance"""
        author = Author.objects.create(name="John Doe", bio="Test bio")

            # Create tag instances
        tag1 = Tag.objects.create(name="test")
        tag2 = Tag.objects.create(name="blog")

        blog_post = BlogPost.objects.create(
            title="Test Post",
            content="This is a test post content",
            author=author,
            created_at=timezone.now(),
        )

        blog_post.tags.set([tag1, tag2]) # Passes tag instances (many to many needs this format)


        self.assertEqual(blog_post.title, "Test Post")
        self.assertEqual(blog_post.content, "This is a test post content")
        self.assertEqual(blog_post.author.name, "John Doe")
        self.assertIsNotNone(blog_post.created_at)
        self.assertEqual(blog_post.tags.count(), 2) # Checks to see if tags are there

    def test_blog_post_author_relation(self):
        """Test the relation between BlogPost and Author"""
        author = Author.objects.create(name="Jane Doe", bio="Bio of Jane")
        blog_post = BlogPost.objects.create(
            title="Blog with Author",
            content="Content with author info",
            author=author,
        )
        self.assertEqual(blog_post.author.name, "Jane Doe")