from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("learn-list/",views.LearnListAPIView.as_view(),name="learn_list"),
    path("learn-detail/",views.LearnDetailAPIView.as_view(),name="detail_list"),
]