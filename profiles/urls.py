from django.urls import path
from . import views

urlpatterns = [path("auth/register/", views.userRegister.as_view(), name="register")]
