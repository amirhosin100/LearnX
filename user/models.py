from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


# Create your models here.

class User(AbstractUser):
    bio = models.TextField(verbose_name="بیوگرافی",blank=True,max_length=500)
    job = models.CharField("شغل",max_length=50,blank=True)
    image = ResizedImageField(verbose_name="تصویر",upload_to="users/images/",blank=True,size=[500,500],crop=["middle","center"],quality=100)
    gived_score_to_films = models.ManyToManyField("learn.LearnFilms",through="learn.FilmScores")

    def get_asks(self,film):
        asks = self.film_asks.filter(film=film)
        return asks



class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="teacher",verbose_name="کاربر")
    score = models.FloatField(default=0,verbose_name="امتیاز")

    phone_number = models.CharField(max_length=11,verbose_name="شماره تماس")
    address = models.TextField(max_length=500,verbose_name="آدرس")

    city = models.CharField(max_length=50,verbose_name="شهر")
    join = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-join']
        indexes = [
            models.Index(fields=['-join'])
        ]
        verbose_name = "مدرس"
        verbose_name_plural = "مدرسان"

    def __str__(self):
        return self.user.get_full_name()

class Bloger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="bloger",verbose_name="کاربر")

    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    address = models.TextField(max_length=500, verbose_name="آدرس")

    city = models.CharField(max_length=50, verbose_name="شهر")
    join = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-join']
        indexes = [
            models.Index(fields=['-join'])
        ]
        verbose_name = "بلاگر"
        verbose_name_plural = "بلاگر ها"

    def __str__(self):
        return self.user.get_full_name()

