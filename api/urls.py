from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"user",views.UserViewSet)
router.register(r"teacher",views.TeacherViewSet)

app_name = "api"

urlpatterns = [
    path("",include(router.urls))
]