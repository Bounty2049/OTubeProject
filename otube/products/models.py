from django.db import models
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images')
    video_url = models.URLField()
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
    # owner = models.ForeignKey(VideoOwner)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# class MyProduct(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=128)
#     description = models.TextField()
#     image = models.ImageField(upload_to='products_images')
#     video_url = models.URLField()
#     category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
#     created_timestamp = models.DateTimeField(auto_now_add=True)
