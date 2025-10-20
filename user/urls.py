from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path("",views.index,name="index"),
    path("about-me/",views.about_me,name="about_me"),
    path("login/",auth_views.LoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("profile/my-asks", views.my_asks, name="my_asks"),
    path("profile/edit-personal-info",views.edit_personal_info,name="edit_personal_info"),
    path("register-courses/",views.register_courses,name="register_courses"),

]
