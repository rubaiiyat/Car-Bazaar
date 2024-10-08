from django.shortcuts import render
from cars.models import carsModel
from django.views.generic import DetailView
from brand.models import brandModel


def home(request, brand_slug=None):
    page = "Home"

    data = carsModel.objects.all()

    if brand_slug is not None:
        brand = brandModel.objects.get(slug=brand_slug)
        data = carsModel.objects.filter(brand=brand)
    brands = brandModel.objects.all()
    return render(request, "home.html", {"page": page, "data": data, "brands": brands})


class postDetails(DetailView):
    model = carsModel
    template_name = "details.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = self.object.name
        return context
