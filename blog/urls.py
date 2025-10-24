from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("detail/<slug:slug>",views.detail,name="detail"),
    path("make-post/",views.make_post,name="make_post"),
    path("edit-post/<int:id>",views.edit_post,name="edit_post"),
    path("like-post/",views.like_post,name="like_post"),
    path("send-comment/",views.send_comment,name="send_comment"),
    path("my-posts/",views.my_posts,name="my_posts"),
]