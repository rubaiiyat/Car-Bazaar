from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("user/", include("profiles.urls")),
    path("user/", include("cars.urls")),
    path("user/", include("cart.urls")),
    path("product/<int:id>", views.postDetails.as_view(), name="Details"),
    path(
        "home/<slug:brand_slug>",
        views.home,
        name="slug_brand",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
