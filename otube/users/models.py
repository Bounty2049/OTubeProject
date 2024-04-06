from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    REQUIRED_FIELDS = (first_name, last_name, email, image)



