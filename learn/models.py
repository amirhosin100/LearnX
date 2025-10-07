from django.db import models
from django_resized import ResizedImageField
from user.models import Teacher
# Create your models here.
class Learn(models.Model):
    teacher = models.ForeignKey(Teacher,models.CASCADE,"learns",verbose_name="مدرس")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    summery_description = models.TextField(max_length=250,verbose_name="خلاصه توضیحات")
    description = models.TextField(max_length=4000,verbose_name="توضیحات")
    image = ResizedImageField(upload_to="learns/images/%Y",size=[1920,1080],crop=["middle","center"],quality=100)
    score = models.FloatField(verbose_name="امتیاز")
    learn_time = models.PositiveIntegerField(verbose_name="مدت زمان آموزش")

    price = models.PositiveIntegerField("قیمت")
    precent_off = models.PositiveIntegerField("درصد تخفیف")
    discount_price = models.PositiveIntegerField("قیمت نهایی")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها"

    def __str__(self):
        return self.title

class Headline(models.Model):
    learn = models.ForeignKey(Learn,models.CASCADE,"headlines")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "سرفصل"
        verbose_name_plural = "سرفصل ها"

    def __str__(self):
        return self.title

def create_url_for_film(instance,filename):
    return f'learns/films/{instance.headline.learn.title}/{instance.headline.title}/{filename}'

class LearnFilms(models.Model):
    headline = models.ForeignKey(Headline,models.CASCADE,"films")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    description = models.TextField(max_length=1200,verbose_name="توضیحات")
    film = models.FileField(upload_to=create_url_for_film)

    score = models.FloatField(default=0,verbose_name="امتیاز")
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    def __str__(self):
        return self.title