from django.core.paginator import Paginator
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
from .forms import LearnForm

def learn_list(request):
    page = request.GET.get('page',1)
    learns = Learn.objects.select_related("teacher__user")
    paginator = Paginator(learns, 4)
    learns = paginator.get_page(page)

    context = {
        'learns': learns,
    }
    return render(request,"learn/list.html",context)

class LearnList(ListView):
    paginate_by = 4
    context_object_name = "learns"
    template_name = "learn/list.html"

    def get_queryset(self):
        query = Learn.objects.prefetch_related("teacher__user")
        date = self.request.GET.get("date","new")
        if date == "old" :
            query = query.order_by("create")
            print(True)
        return query
    def get_context_data(self,**kwargs):
        date = self.request.GET.get("date","new")
        context = super().get_context_data(**kwargs)

        context["date"] = date
        return context

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
        num = tags.to_persian_numbers(film.number_score)
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
    return render(request,"forms/make_learn.html")
