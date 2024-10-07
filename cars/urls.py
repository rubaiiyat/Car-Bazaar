from django.urls import path
from . import views

urlpatterns = [path("addcar/", views.addCars.as_view(), name="addcar")]
