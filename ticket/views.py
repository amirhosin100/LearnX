from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.
@login_required
def my_tickets(request):
    return render(request,"pages/my_tickets.html")

@login_required
def new_simple_ticket(request):
    if request.method == "POST" :
        s_form = SimpleTicketForm(request.POST)
        a_form = AnswerTicketForm(request.POST)
        if a_form.is_valid() and s_form.is_valid() :
            ticket = s_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            answer = a_form.save(commit=False)
            answer.user = request.user
            answer.ticket = ticket
            answer.save()
            messages.success(request,"تیکت شما با موفقیت ارسال شد")
            return redirect("ticket:my_ticket")
    else:
        s_form = SimpleTicketForm()
        a_form = AnswerTicketForm()
    context = {
        "s_form" :s_form,
        "a_form": a_form,
    }
    return render(request,"forms/new_simple_ticket.html",context)

@login_required
def detail(request,id):
    ticket = get_object_or_404(SimpleTicket,id=id)
    if ticket.user == request.user :
        context = {
            "ticket" :ticket,
        }
        return render(request,"pages/ticket_detail.html",context)
    else:
        return redirect("ticket:my_ticket")

@login_required
@require_POST
def send_answer(request):
    ticket_id = request.POST.get("ticket_id")
    ticket = SimpleTicket.objects.get(id=ticket_id)
    form = AnswerTicketForm(request.POST)
    if form.is_valid() :
        answer =form.save(commit=False)
        answer.ticket = ticket
        answer.user = request.user
        answer.save()

    return redirect("ticket:detail",ticket_id)

@login_required
def collaboration(request):
    if request.method == "POST" :
        form = CollaborationTicketForm(request.POST)
        if form.is_valid():
            collaboration = form.save(commit=False)
            collaboration.user = request.user
            collaboration.save()
            messages.success(request,"درخواست شما ارسال شد و پس از تایید با شما تماس گرفته می شود")
            return redirect("user:index")
    else:
        form  = CollaborationTicketForm()

    context = {
        "form":form,
    }
    return render(request,"forms/collaboration.html",context)