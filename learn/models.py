from django.db import models
from django_resized import ResizedImageField
from user.models import Teacher,User
from django.urls import reverse
from django_jalali.db import models as jmodels
from django.db.models import Count,Avg


# Create your models here.
class Learn(models.Model):
    teacher = models.ForeignKey(Teacher,models.CASCADE,"learns",verbose_name="مدرس")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    summery_description = models.TextField(max_length=250,verbose_name="خلاصه توضیحات")
    description = models.TextField(max_length=4000,verbose_name="توضیحات")
    image = ResizedImageField(upload_to="learns/images/%Y",size=[1920,1080],crop=["middle","center"],quality=100)
    score = models.FloatField(verbose_name="امتیاز")
    learn_time = models.PositiveIntegerField(verbose_name="مدت زمان آموزش")

    slug = models.SlugField("اسلاگ")

    price = models.PositiveIntegerField("قیمت")
    precent_off = models.PositiveIntegerField("درصد تخفیف")
    discount_price = models.PositiveIntegerField("قیمت نهایی")
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('learn:learn_detail', args=[self.slug])

class Headline(models.Model):
    learn = models.ForeignKey(Learn,models.CASCADE,"headlines")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    create = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "سرفصل"
        verbose_name_plural = "سرفصل ها"

    def __str__(self):
        return f"{self.learn.title} : {self.title}"

def create_url_for_film(instance,filename):
    return f'learns/films/{instance.headline.learn.title}/{instance.headline.title}/{filename}'

class LearnFilms(models.Model):
    headline = models.ForeignKey(Headline,models.CASCADE,"films",verbose_name="سرفصل")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    description = models.TextField(max_length=1200,verbose_name="توضیحات")
    film = models.FileField("فیلم",upload_to=create_url_for_film)

    create = jmodels.jDateTimeField(auto_now_add=True)
    scores = models.ManyToManyField(User,through="FilmScores")
    number_score = models.FloatField("امتیاز",default=0)

    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    def get_absolute_url(self):
        return reverse('learn:film_detail', args=[self.headline.learn.slug, self.id])

    def __str__(self):
        return f"{self.headline.learn.title} : {self.headline.title} : {self.title}"

class FilmScores(models.Model):
    film_to = models.ForeignKey(LearnFilms,models.CASCADE,"rel_to_set")
    user_from = models.ForeignKey(User,models.CASCADE,"rel_from_set")
    SCORES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    score = models.PositiveIntegerField("امتیاز",choices=SCORES,max_length=1,default=1)

    def __str__(self):
        return f"{self.user_from.username} : {self.score}"

    class Meta:
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازات"

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        film = self.film_to
        scores = FilmScores.objects.filter(film_to=film)
        number = scores.aggregate(Avg("score"))
        film.number_score = number["score__avg"]
        film.save()

