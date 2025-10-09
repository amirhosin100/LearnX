from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.

class CommentForLearnManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class CommentForLearn(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE,
                             related_name='learn_comments',verbose_name="کاربر")
    learn = models.ForeignKey("learn.Learn", on_delete=models.CASCADE,
                              related_name='comments',verbose_name="آموزش")

    content = models.TextField(max_length=500,verbose_name="پیام")
    super_comment = models.ForeignKey("self", on_delete=models.CASCADE,related_name="sub_comment",blank=True,null=True)

    create = jmodels.jDateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False,verbose_name="وضعیت")

    objects = jmodels.jManager()
    publish = CommentForLearnManager()
    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create']),
        ]
        verbose_name = "نظر برای آموزش"
        verbose_name_plural = "نظرات برای آموزش"

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.content[:20]}"

class AskForFilm(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE,
                             verbose_name="کاربر",related_name="film_asks")
    film = models.ForeignKey("learn.LearnFilms", on_delete=models.CASCADE,
                             verbose_name="فیلم",related_name="asks")

    content = models.TextField(max_length=500)
    create = jmodels.jDateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "سوال آموزش"
        verbose_name_plural = "سوالات آموزش"

    def __str__(self):
        return f"{self.user.get_full_name()} : {self.content[:20]}"

class AnswerForFilm(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE,
                             verbose_name="مدرس یا پشتیبان",related_name="film_answers")
    ask = models.ForeignKey(AskForFilm, on_delete=models.CASCADE,
                            verbose_name="سوال",related_name="answers")
    content = models.TextField(max_length=500)
    create = jmodels.jDateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create']),
        ]
        verbose_name = "پاسخ"
        verbose_name_plural = 'پاسخ ها'

    def __str__(self):
        return f"{self.ask.content[:20]} : {self.content[:20]}"