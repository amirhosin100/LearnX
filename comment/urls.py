from django.urls import path
from . import views
app_name = 'comment'

urlpatterns = [
    path("send_comment_for_learn/",views.send_comment_for_learn,name="send_comment_for_learn"),
    path("send_ask_for_film/",views.send_ask_for_film,name="send_ask_for_film"),
]