from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey("user.User",models.CASCADE,"orders",verbose_name="کاربر")
    price = models.PositiveIntegerField("مبلغ")
    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name="تاریخ")
    description = models.TextField(max_length=500,verbose_name="توضیحات")
    paid = models.BooleanField(verbose_name="وضعیت پرداخت",default=True)

    class Meta:
        ordering = [
            "-create"
        ]
        indexes = [
            models.Index(fields=[
                "-create"
            ])
        ]
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"

    def __str__(self):
        return f"{self.user} : {self.create}"

class LearnOrder(models.Model):
    order = models.ForeignKey(Order,models.CASCADE,"learns",verbose_name="برای تراکنش:")
    learn = models.ForeignKey("learn.Learn",models.CASCADE,verbose_name="آموزش")

    class Meta:
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها"

class OffCode(models.Model):
    code = models.CharField(max_length=15,verbose_name="کد تخفیف")
    value = models.PositiveIntegerField("مقدار تخفیف")

    create = jmodels.jDateTimeField("تاریخ ایجاد",default=jmodels.timezone.now)
    date_end = jmodels.jDateTimeField("تاریخ انقضا",default=jmodels.timezone.now)

    objects = jmodels.jManager()

    class Meta:
        ordering = [
            "-create",
        ]
        indexes = [
            models.Index(fields=[
                "-create"
            ]),
            models.Index(fields=[
                "-date_end"
            ])
        ]
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کد های تخفیف"

    def __str__(self):
        return self.code