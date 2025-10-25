from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.
@login_required
def new_simple_ticket(request):
    if request.method == "POST" :
        form = SimpleTicketForm(request.POST)
        if form.is_valid() :
            ticket =form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request,"تیکت شما با موفقیت ارسال شد")
            return redirect("user:profile")
    else:
        form = SimpleTicketForm()
    context = {
        "form" :form
    }
    return render(request,"forms/new_simple_ticket.html",context)