from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from learn.models import Learn,LearnFilms
# Create your views here.

@require_POST
@login_required
def send_comment_for_learn(request):
    print(True)
    user = request.user
    learn_id = request.POST.get("learn_id")
    comment = request.POST.get("comment")
    if comment:
        try:
            learn = get_object_or_404(Learn, id=learn_id)
            comment = CommentForLearn(learn=learn,user=user, content=comment)
            comment.save()
            return JsonResponse({"status":"نظر شما با موفقیت ثبت گردید و پس از تایید نمایش داده خواهد شد."})
        except :
            return JsonResponse({"error":"Error"})
    else:
        return JsonResponse({"error": "comment was empty"})


@login_required
@require_POST
def send_ask_for_film(request):
    user = request.user
    film_id = request.POST.get("film_id")
    message = request.POST.get("message")
    print(message)
    if message:
        try:
            print("true")
            film = get_object_or_404(LearnFilms, id=film_id)
            print("true")
            comment = AskForFilm(film=film, user=user, content=message)
            comment.save()
            return JsonResponse({"message":"سوال شما ارسال شد و پس از پاسخ به شما نمایش داده میشود"})

        except :
            return JsonResponse({"error":"Error"})
    else:
        return JsonResponse({"error": "comment was empty"})
