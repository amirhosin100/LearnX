from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users",views.UserViewSet)
router.register("teachers",views.TeacherViewSet)
router.register("blogers",views.BlogerViewSet)
router.register("learns",views.LearnViewSet)
router.register("headlines",views.HeadlineViewSet)


urlpatterns = [
    path("",include(router.urls)),
]