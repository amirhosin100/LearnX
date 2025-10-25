from django.urls import path
from . import views

app_name = "ticket"

urlpatterns = [
    path("new-simple-ticket/",views.new_simple_ticket,name="new_simple_ticket"),
]