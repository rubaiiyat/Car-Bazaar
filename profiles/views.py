from django.shortcuts import redirect
from django.urls import reverse_lazy
from .form import userForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Create your views here.
class userRegister(CreateView):
    form_class = userForm
    template_name = "userform.html"
    success_url = reverse_lazy("register")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Register"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successfully")
        return super().form_valid(form)


class userLogin(LoginView):
    template_name = "userform.html"

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Login"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfull")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Username or Password")
        return super().form_invalid(form)


class userProfile(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "profile"
        return context


def userLogout(request):
    if request.user.is_authenticated:

        logout(request)
        messages.success(request, "Logged Out")
        return redirect("login")
