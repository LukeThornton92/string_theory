from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colour = models.CharField(max_length=50, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body_material = models.CharField(max_length=100, null=True, blank=True)
    neck_material = models.CharField(max_length=100, null=True, blank=True)
    fretboard_material = models.CharField(max_length=100, null=True, blank=True)
    scale_length = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    num_of_frets = models.IntegerField(null=True, blank=True)
    pickups = models.CharField(max_length=100, null=True, blank=True)
    neck_shape = models.CharField(max_length=100, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name
