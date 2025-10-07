from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import *
from learn.models import *

# Create your views here.

def index(request):
    courses = Learn.objects.all()[:4]
    context = {
        "courses": courses,
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

