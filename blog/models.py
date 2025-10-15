from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_jalali.db import models as jmodels
# Create your models here.
class Post(models.Model):
    bloger = models.ForeignKey("user.Bloger",models.PROTECT,"posts",verbose_name="بلاگر")

    title = models.CharField("عنوان",max_length=250)
    summery_description = models.CharField("خلاصه پست")
    body = CKEditor5Field(config_name='default')
    status = models.BooleanField(verbose_name="وضعیت",default=True)

    #dates
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title[:50]