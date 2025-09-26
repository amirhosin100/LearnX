from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):

    class User_types(models.TextChoices):
        NORMAL = "NORMAL" , "عادی"
        TEACHER = "TEACHER" , "مدرس"
        BLOGER = "BLOGER" , "بلاگر"
        MANAGER =  "MANAGER" , "مدیر"

    user_type = models.CharField(verbose_name="نوع کاربر",choices = User_types.choices ,default=User_types.NORMAL, max_length=10)
    bio = models.TextField(verbose_name="بیوگرافی",blank=True,max_length=500)
    image = ResizedImageField(verbose_name="تصویر",upload_to="users/images/",blank=True,size=[500,500],crop=["middle","center"],quality=100)
