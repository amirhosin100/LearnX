from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import *
# Create your views here.
def learn_list(request):
    return HttpResponse("Learn List")

def learn_detail(request,slug_learn):
    learn = get_object_or_404(Learn,slug=slug_learn)
    context = {
        "learn": learn,
    }
    return render(request,"learn/learn_detail.html",context)

def film_detail(request,slug_learn,id):
    film = get_object_or_404(LearnFilms,id=id)
    learn = get_object_or_404(Learn,slug=slug_learn)
    context = {
        "film": film,
        "learn": learn,
    }
    return render(request,"learn/film_detail.html",context)