from django.db import models

# Create your models here.
class Post(models.Model):
    bloger = models.ForeignKey("user.Bloger",models.PROTECT,"posts",verbose_name="بلاگر")

    title = models.CharField("عنوان",max_length=250)
    summery_description = models.CharField("خلاصه پست")