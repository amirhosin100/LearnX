from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Prefetch
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from comment.models import CommentForLearn,AnswerForFilm
from django.views.generic.list import ListView
from .templatetags import tags
# Create your views here.
from decorators.users import checking_register_learn
from decorators.teachers import Is_tacher
from .forms import *
from django.contrib import messages
import json

def check_teacher(request,learn):
    if learn.teacher.user == request.user or request.user.is_superuser:
        return True
    else:
        return redirect("user:profile")


class LearnList(ListView):
    paginate_by = 4
    context_object_name = "learns"
    template_name = "learn/list.html"

    def get_queryset(self):
        query = Learn.objects.prefetch_related("teacher__user")
        # for date
        date = self.request.GET.get("date","new")
        if date == "old" :
            query = query.order_by("create")
        #----
        #for only_free
        only_free = self.request.GET.get("only_free")
        if only_free == "on" :
            query = query.filter(discount_price=0)
        return query

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
            )).
        prefetch_related("attributes"),slug=slug_learn
    )

    context = {
        "learn": learn,
    }
    return render(request,"learn/learn_detail.html",context)

@login_required
@checking_register_learn
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
        num = tags.to_persian_numbers(tags.check_int(film.number_score))
        return JsonResponse({"score": num})

    except :
        return JsonResponse({"error": "Error"})

@login_required
@Is_tacher
def make_learn(request):
    if request.method == "POST" :
        form = LearnForm(request.POST,files=request.FILES)
        if form.is_valid() :
            print(True)
            learn = form.save(commit=False)
            print(True)
            learn.teacher = request.user.teacher
            print(True)
            learn.save()
            return redirect("user:profile")
    else:
        form = LearnForm()
    context = {
        "form":form
    }
    return render(request,"forms/make_learn.html",context)

@login_required
@Is_tacher
def my_learns(request):
    return render(request,"teacher_profile/my-learns.html")


@login_required
def detail_for_teacher(request,id):
    learn = get_object_or_404(
        Learn.objects.prefetch_related(
            Prefetch(
                "headlines",
                queryset=Headline.objects.prefetch_related("films")
            )
        ),
        id=id
    )
    if learn.teacher == request.user.teacher or request.user.is_superuser:
        context = {
            "learn" : learn ,
        }
        return render(request,"teacher_profile/learn_detail_for_teacher.html",
                      context)
    else:
        return redirect("user:profile")

@login_required
def edit_learn(request,slug):
    learn = get_object_or_404(Learn,slug=slug)
    if request.method == "POST" :
        form = LearnForm(request.POST,instance=learn,files=request.FILES)
        if form.is_valid():
            learn = form.save()
            messages.success(request,f"دوره ی {learn.title} با موفیقت تغییر پیدا کرد")
            return redirect("learn:my_learns")
    else:
        form = LearnForm(instance=learn)

    context = {
        "form" :form,
        "edit" : True ,
    }
    return render(request,"forms/make_learn.html",context)


# noinspection PyTypeChecker
def make_film(request,h_id):
    headline = get_object_or_404(Headline.objects.select_related("learn__teacher__user"),id=h_id)
    response = check_teacher(request,headline.learn)

    if response == True :
        if request.method == "POST":
            form = FilmForm(request.POST,request.FILES)
            if form.is_valid() :
                film = form.save(commit=False)
                film.headline = headline
                film.save()
                messages.success(request,"ویدئو با موفقیت ایجاد شد")
                return redirect("learn:detail_for_teacher",headline.learn.id)
        else:
            form = FilmForm()
        context = {
            "form":form,
        }
        return render(request,"forms/make_film.html",context)
    else:
        return response

@login_required
@require_POST
def make_headline(request,learn_id):
    learn = get_object_or_404(Learn,id=learn_id)
    data = json.loads(request.body)
    title = data.get("title")
    if title :
        try :
            headline = Headline.objects.create(learn=learn,title=title)
            num = tags.to_persian_numbers(learn.headlines.count())
            return JsonResponse({"status":"created","number":num,"id":headline.id})
        except :
            JsonResponse({"error":"Somethings went wrong"})
    else :
        return JsonResponse({"error":"title is null"})

@login_required
def edit_film(request,id):
    film = get_object_or_404(LearnFilms.objects.select_related("headline__learn__teacher__user"),id=id)
    response = check_teacher(request,film.headline.learn)
    if response == True:
        if request.method == "POST":
            form = FilmForm(request.POST,instance=film,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,f"ویدئو <{form.instance.title}> با موفقیت ویرایش شد")
                return redirect("learn:detail_for_teacher",film.headline.learn.id)
        else:
            form = FilmForm(instance=film)

        context = {
            "form" :form,
            "edit" : True,
        }
        return render(request,"forms/make_film.html",context)
    else:
        return response