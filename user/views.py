from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import *
from learn.models import Learn
from blog.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #فقط چهار مورد
    courses = Learn.objects.all().select_related("teacher__user")[:4]
    posts =  Post.objects.all()[:4]
    context = {
        "courses": courses,
        "posts" :posts,
    }
    return render(request,"pages/main_page.html",context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("user:index")
    else :
        form = RegisterForm()

    context = {"form":form}
    return render(request,"registration/register.html",context)

@login_required
def profile(request):
    return render(request,"profile/main_profile_page.html")

@login_required
def your_asks(request):
    return render(request,"profile/your_asks.html")

@login_required
def edit_personal_info(request):
    if request.method == "POST":
        form = EditUserForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user:profile")
    else:
        form = EditUserForm(instance=request.user)

    context = {
        "form" :form
    }
    return render(request,"profile/edit_personal_info_user.html",context)