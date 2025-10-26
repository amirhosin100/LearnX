from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import FilmScores,LearnFilms,Learn
from django.db.models import Avg

@receiver(post_save,sender=FilmScores)
def set_score(sender,instance,**kwargs):
    film = instance.film_to
    scores = FilmScores.objects.filter(film_to=film)
    number = scores.aggregate(Avg("score"))
    film.number_score = number["score__avg"]
    film.save()
    # for learn
    learn = film.headline.learn
    films = LearnFilms.objects.filter(headline__learn=learn)
    number = films.aggregate(Avg("number_score"))
    learn.score = number["number_score__avg"]
    learn.save()
    # for teacher
    teacher = learn.teacher
    learns = Learn.objects.filter(teacher=teacher)
    number = learns.aggregate(Avg("score"))
    teacher.score = number["score__avg"]
    teacher.save()
