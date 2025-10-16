from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_jalali.db import models as jmodels
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    bloger = models.ForeignKey("user.Bloger",models.PROTECT,"posts",verbose_name="بلاگر")

    title = models.CharField("عنوان",max_length=250)
    summery_description = models.CharField("خلاصه پست")
    body = CKEditor5Field(config_name='default',verbose_name="بدنه اصلی")
    status = models.BooleanField(verbose_name="وضعیت",default=True)

    slug = models.SlugField(verbose_name="اسلاگ")

    main_image = ResizedImageField("تصویر",upload_to="blog/main_image/",
                                   size=[1920,1080],quality=100,crop=["middle","center"])

    likes = models.ManyToManyField("user.User","liked_posts",verbose_name="لایک ها",blank=True)
    #dates
    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    update = jmodels.jDateTimeField(auto_now=True,verbose_name="تاریخ آخرین آپدیت")



    def get_absolute_url(self):
        return reverse("blog:detail",args=[self.slug])

    class Meta:
        ordering = [
            "-create"
        ]
        indexes = [
            models.Index(fields=[
                "-create"
            ])
        ]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title[:50]