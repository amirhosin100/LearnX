from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users",views.UserViewSet)
router.register(r"teachers",views.TeacherViewSet)
router.register(r"posts",views.PostViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path("send-ticket/",views.TicketView.as_view()),
    path("my-posts/",views.PostListView.as_view()),
]