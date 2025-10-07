from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_list(request):
    return HttpResponse("Learn List")

def learn_detail(request,slug):
    return render(request,"learn/detail.html")

def film_detail(request,slug):
    return render(request,"learn/detail.html")