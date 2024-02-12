from django.db import models
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    preview = models.ImageField(upload_to='products_images')
    video = models.FileField(upload_to='products_videos')
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images')
    video_url = models.URLField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'library for {self.user.username} | Product: {self.product.title}'
