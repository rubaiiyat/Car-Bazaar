from django.urls import path
from . import views

urlpatterns = [path("add_to_cart/<int:product_id>", views.addToCart, name="addtocart")]
