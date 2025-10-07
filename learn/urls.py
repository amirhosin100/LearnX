from django.urls import path
from . import views

app_name = "learn"

urlpatterns = [
    path('list/', views.learn_list, name='index'),
    path("detail/<slug:slug_learn>", views.learn_detail, name='learn_detail'),
    path("detail/<slug:slug_learn>/<int:id>",views.film_detail, name='film_detail'),
]