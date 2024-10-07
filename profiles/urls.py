from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.userRegister.as_view(), name="register"),
    path("auth/login/", views.userLogin.as_view(), name="login"),
    path("profile", views.userProfile.as_view(), name="profile"),
    path("auth/logout/", views.userLogout, name="logout"),
]
