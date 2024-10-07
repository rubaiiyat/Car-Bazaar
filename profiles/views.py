from django.shortcuts import render


# Create your views here.
def register(request):
    page = "Register"
    return render(request, "userform.html", {"page": page})
