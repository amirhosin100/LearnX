from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("detail/<int:id>",views.detail,name="detail"),
    path("make-post/",views.make_post,name="make_post"),
]