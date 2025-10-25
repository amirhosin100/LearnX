from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.
class SimpleTicket(models.Model):
    user = models.ForeignKey("user.User",models.SET_NULL,
                             "tickets",null=True,verbose_name="کاربر")
    categories = (
        ("نظر","نظر"),
        ("انتقاد", "انتقاد"),
        ("پیشنهاد", "پیشنهاد"),
    )
    category = models.CharField(max_length=10,choices=categories,verbose_name="دسته بندی")
    message = models.TextField(max_length=500,verbose_name="پیام")

    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name="تاریخ ارسال")

    class Meta :
        ordering = [
            "-create"
        ]
        indexes = [
            models.Index(fields=["-create"])
        ]
        verbose_name = "تیک"
        verbose_name_plural = "تیکت ها"

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.message[:30]}"

class TeacherTicket(models.Model):
    user = models.ForeignKey("user.User", models.SET_NULL, null=True, verbose_name="کاربر")
    first_name = models.CharField(max_length=255,verbose_name="نام")
    last_name = models.CharField(max_length=255,verbose_name="نام خانوادگی")
    age = models.CharField(max_length=2,verbose_name="سن")
    city = models.CharField(max_length=30,verbose_name="شهر")
    address = models.TextField(max_length=500,verbose_name="آدرس")
    phone = models.CharField(max_length=11,verbose_name="شماره تلفن")
    bio = models.TextField(max_length=1000,verbose_name="بیوگرافی")

    create = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")

    class Meta:
        ordering = [
            "-create"
        ]
        indexes = [
            models.Index(fields=["-create"])
        ]
        verbose_name = "درخواست مدرس"
        verbose_name_plural = "درخواست مدرسان"

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.phone}"
