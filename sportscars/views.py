from django.shortcuts import render
from cars.models import carsModel


def home(request):
    page = "Home"

    data = carsModel.objects.all()
    return render(request, "home.html", {"page": page, "data": data})
