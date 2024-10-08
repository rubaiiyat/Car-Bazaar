from django.shortcuts import render
from cars.models import carsModel
from django.views.generic import DetailView


def home(request):
    page = "Home"

    data = carsModel.objects.all()
    return render(request, "home.html", {"page": page, "data": data})


class postDetails(DetailView):
    model = carsModel
    template_name = "details.html"
    pk_url_kwarg = "id"
