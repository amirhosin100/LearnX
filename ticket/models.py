from django.db import models
from django_jalali.db import models as jmodels
from django.urls import reverse
# Create your models here.
class SimpleTicket(models.Model):
    user = models.ForeignKey("user.User",models.SET_NULL,
                             "tickets",null=True,verbose_name="کاربر")
    categories = (
        ("نظر","نظر"),
        ("انتقاد", "انتقاد"),
        ("پیشنهاد", "پیشنهاد"),
    )
    statuses = (
        ("new","جدید"),
        ("processing","درحال پردازش"),
        ("closed", "بسته شده"),
    )
    category = models.CharField(max_length=10,choices=categories,verbose_name="دسته بندی")
    title = models.CharField(max_length=100,verbose_name="عنوان")
    status = models.CharField(max_length=15,choices=statuses,verbose_name="وضعیت",default="new")

    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name="تاریخ ارسال")

    class Meta :
        ordering = [
            "-create"
        ]
        indexes = [
            models.Index(fields=["-create"])
        ]
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"

    def get_absolute_url(self):
        return reverse("ticket:detail",args=[self.id])

    def __str__(self):
        return self.title

class AnswerTicket(models.Model):
    user = models.ForeignKey("user.User",models.PROTECT,verbose_name="کاربر")
    ticket = models.ForeignKey(SimpleTicket,models.CASCADE,verbose_name="تیکت",related_name="answers")
    message = models.TextField(max_length=1000,verbose_name="پیام")
    create = jmodels.jDateTimeField(auto_now_add=True)

    class Meta :
        ordering = [
            "create"
        ]
        indexes = [
            models.Index(fields=["create"])
        ]
        verbose_name = "پاسخ به تیکت"
        verbose_name_plural = "پاسخ ها به تیکت"

    def __str__(self):
        return f"{self.ticket.title} : {self.message[:30]}"

class CollaborationTicket(models.Model):

    class TYPES(models.TextChoices):
        TH = "teacher","مدرس"
        BL = "bloger" , "بلاگر"

    user = models.ForeignKey("user.User", models.SET_NULL, null=True, verbose_name="کاربر")
    type = models.CharField(max_length=10,choices=TYPES.choices,verbose_name="نوع همکاری")
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
        verbose_name = "درخواست همکاری"
        verbose_name_plural = "درخواست های همکاری"

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.phone}"
