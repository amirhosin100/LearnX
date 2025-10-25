from django.urls import path
from . import views

app_name = "ticket"

urlpatterns = [
    path("my-tickets/",views.my_tickets,name="my_ticket"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("new-simple-ticket/",views.new_simple_ticket,name="new_simple_ticket"),
    path("send-answer/",views.send_answer,name="send_answer"),
    path("collaboration/",views.collaboration,name="collaboration"),
]