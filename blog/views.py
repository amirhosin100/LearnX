import json

from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import *
from .forms import *
from comment.models import CommentForPost
from decorators.blogers import Is_bloger
# Create your views here.

def detail(request,slug):
    post = get_object_or_404(Post.objects.select_related("bloger__user"),slug=slug)
    comments = CommentForPost.publish.filter(post=post).select_related("user").all()
    context = {
        "post":post,
        "comments" : comments
    }
    return render(request,"pages/post_detail.html",context)

@login_required
@Is_bloger
def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.bloger = request.user.bloger
            post.save()
            return redirect("user:index")
    else:
        form = PostForm()

    context = {
        "form" :form,
    }
    return render(request,"forms/make_post.html",context)

@require_POST
@login_required
def like_post(request):
    post_id = request.POST.get("post_id")
    user = request.user
    post = get_object_or_404(Post,id=post_id)
    like = False
    try:
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
            like = True
        return JsonResponse({"like":like})
    except :
        return JsonResponse({"Error":"error"})


@require_POST
def send_comment(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        post_id = data.get("post_id")
        user = request.user
        post = get_object_or_404(Post,id=post_id)
        content = data.get("content")
        if content :
            try :
                CommentForPost.objects.create(user=user,post=post,content=content)
                print(True)
                return JsonResponse({"status":"نظر شما با موفقیت ارسال شد و پس از تایید نمایش داده می شود"})
            except:
                return JsonResponse({"error": "error"})
        else:
            return JsonResponse({"error":"error"})
    else:
        return JsonResponse({"status": "ابتدا در سایت لاگین کنید!"})

@login_required
@Is_bloger
def my_posts(request):
    return render(request,"pages/my_posts.html")