from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.db.models import Prefetch
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import *
from comment.models import CommentForLearn,AnswerForFilm
# Create your views here.
def learn_list(request):
    return HttpResponse("Learn List")

def learn_detail(request,slug_learn):
    learn = get_object_or_404(
        Learn.objects.select_related("teacher__user").
        prefetch_related(
            Prefetch(
                'headlines',
                queryset=Headline.objects.prefetch_related('films')
            )
        ).
        prefetch_related(
            Prefetch(
                "comments",
                queryset= CommentForLearn.publish.prefetch_related("user")
            )),slug=slug_learn
    )

    context = {
        "learn": learn,
    }
    return render(request,"learn/learn_detail.html",context)

def film_detail(request,slug_learn,id):
    film = get_object_or_404(LearnFilms.objects,id=id,headline__learn__slug=slug_learn)
    learn = get_object_or_404(
        Learn.objects.select_related("teacher__user").prefetch_related(
            Prefetch(
                "headlines",
                queryset=Headline.objects.prefetch_related("films")
            )
        ),
        slug=slug_learn)

    number_score = 0
    asks = request.user.get_asks(film).prefetch_related(
        Prefetch(
            "answers",
            queryset=AnswerForFilm.objects.prefetch_related("user")
        )
    )
    if film in request.user.gived_score_to_films.all() :
        number_score =FilmScores.objects.get(film_to=film,user_from=request.user).score
    context = {
        "film": film,
        "learn": learn,
        "number_score": number_score,
        "asks": asks,
    }
    return render(request,"learn/film_detail.html",context)

@require_POST
@login_required
def send_score(request):
    id_film = request.POST.get("film_id")
    user = request.user
    score = int(request.POST.get("score"))
    film = get_object_or_404(LearnFilms,id=id_film)
    try :
        if user not in film.scores.all() :
            print(True)
            FilmScores(user_from=user,film_to=film,score=score).save()

        else:
            item = FilmScores.objects.get(film_to=film,user_from=user)
            item.score = score
            item.save()
        film = LearnFilms.objects.get(id=id_film)
        return JsonResponse({"score": film.number_score})

    except :
        return JsonResponse({"error": "Error"})



