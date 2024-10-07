from django.urls import reverse_lazy
from .form import userForm
from django.views.generic import CreateView, TemplateView


# Create your views here.
class userRegister(CreateView):
    form_class = userForm
    template_name = "userform.html"
    success_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Register"
        return context
