from django.shortcuts import render, redirect
from cars.models import carsModel
from django.views.generic import DetailView
from brand.models import brandModel
from cars.forms import commentForm


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

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = commentForm(data=self.request.POST)

        if comment_form.is_valid():
            newComment = comment_form.save(commit=False)
            newComment.post = post
            newComment.save()
            return redirect("Details", id=post.id)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = commentForm()

        context["page"] = self.object.name
        context["comments"] = comments
        context["form"] = comment_form
        return context
