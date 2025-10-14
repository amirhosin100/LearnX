from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("",views.index,name="index"),
    path("add/",views.add_remove_learn_to_cart,name="add_or_remove"),
    path("buy/",views.buy,name="buy"),
]