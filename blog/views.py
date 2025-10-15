from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
# Create your views here.

def detail(request,id):
    post = get_object_or_404(Post,id=id)
    context = {
        "post":post
    }
    return render(request,"pages/post_detail.html",context)

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
