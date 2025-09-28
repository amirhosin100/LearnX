from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(verbose_name="بیوگرافی",blank=True,max_length=500)
    image = ResizedImageField(verbose_name="تصویر",upload_to="users/images/",blank=True,size=[500,500],crop=["middle","center"],quality=100)
