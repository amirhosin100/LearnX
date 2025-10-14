from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",auth_views.LoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("profile/your-asks",views.your_asks,name="your_asks"),
    path("profile/edit-personal-info",views.edit_personal_info,name="edit_personal_info")
]
