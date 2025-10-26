from django.db import models
from django_resized import ResizedImageField
from user.models import Teacher,User
from django.urls import reverse
from django_jalali.db import models as jmodels
from django_ckeditor_5.fields import CKEditor5Field

def create_url_for_film(instance,filename):
    return f'learns/films/{instance.headline.learn.title}/{instance.headline.title}/{filename}'

# Create your models here.
class Learn(models.Model):
    teacher = models.ForeignKey(Teacher,models.CASCADE,"learns",verbose_name="مدرس")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    summery_description = models.TextField(max_length=250,verbose_name="خلاصه توضیحات")
    description = CKEditor5Field(max_length=4000,verbose_name="توضیحات",config_name="learn")
    image = ResizedImageField(upload_to="learns/images/%Y",size=[1920,1080],crop=["middle","center"],quality=100)
    score = models.FloatField(verbose_name="امتیاز",default=5)
    learn_time = models.PositiveIntegerField(verbose_name="مدت زمان آموزش")

    slug = models.SlugField("اسلاگ",unique=True)

    price = models.PositiveIntegerField("قیمت")
    precent_off = models.PositiveIntegerField("درصد تخفیف",default=0)
    discount_price = models.PositiveIntegerField("قیمت نهایی",default=0)

    #many to many

    users_register = models.ManyToManyField("user.User","learns",through="RegisterLearn")

    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    objects = jmodels.jManager()

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

    #برای زمانی که مدرس می خواهد جزیات دوره اش را ببیند
    def get_detail_url(self):
        return reverse("learn:detail_for_teacher",args=[self.id])

    def save(self ,*args,**kwargs):
        self.discount_price = self.price - (self.price * self.precent_off / 100)
        super().save(*args,**kwargs)

class Headline(models.Model):
    learn = models.ForeignKey(Learn,models.CASCADE,"headlines")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    create = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create']
        indexes = [
            models.Index(fields=['create'])
        ]
        verbose_name = "سرفصل"
        verbose_name_plural = "سرفصل ها"

    def __str__(self):
        return f"{self.learn.title} : {self.title}"

class LearnFilms(models.Model):
    headline = models.ForeignKey(Headline,models.CASCADE,"films",verbose_name="سرفصل")
    title = models.CharField(max_length=255,verbose_name="عنوان")
    description = CKEditor5Field(config_name="film",max_length=1200,verbose_name="توضیحات")
    film = models.FileField("فیلم",upload_to=create_url_for_film)

    create = jmodels.jDateTimeField(auto_now_add=True)
    scores = models.ManyToManyField(User,through="FilmScores")
    number_score = models.FloatField("امتیاز",default=5)

    class Meta:
        ordering = ['create']
        indexes = [
            models.Index(fields=['create'])
        ]
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    def get_absolute_url(self):
        return reverse('learn:film_detail', args=[self.headline.learn.slug, self.id])

    def __str__(self):
        return f"{self.headline.learn.title} : {self.headline.title} : {self.title}"

class FilmScores(models.Model):
    film_to = models.ForeignKey(LearnFilms,models.CASCADE,"score_to_set")
    user_from = models.ForeignKey(User,models.CASCADE,"film_from_set")
    SCORES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    score = models.PositiveIntegerField("امتیاز",choices=SCORES,default=1)

    def __str__(self):
        return f"{self.user_from.username} : {self.score}"

    class Meta:
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازات"





class attribute(models.Model):
    learn = models.ForeignKey(Learn,models.CASCADE,"attributes",verbose_name="آموزش")
    value = models.CharField(max_length=30,verbose_name="مقدار")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

    def __str__(self):
        return f"{self.learn.title} : {self.value}"

# ایجاد یک مدل واسط برای کاربری که در دوره ها شرکت کرده است و برعکس(دوره ای که چند کاربر دارد)

class RegisterLearn(models.Model):
    user_from = models.ForeignKey(User,models.CASCADE,related_name="register_from_set")
    learn_to = models.ForeignKey(Learn,models.CASCADE,related_name="register_to_set")
    date_of_register = jmodels.jDateTimeField(auto_now_add=True)
    objects = jmodels.jManager()

