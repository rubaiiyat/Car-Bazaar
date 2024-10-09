from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import carsForm, commentForm
from django.views.generic import CreateView
from django.contrib import messages
from cars.models import carsModel, commentModel


class addCars(CreateView):
    form_class = carsForm
    template_name = "carform.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("addcar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Add Cars"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Item Added")
        return super().form_valid(form)
