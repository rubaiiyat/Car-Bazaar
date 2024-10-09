from django.shortcuts import render, redirect, get_object_or_404
from .models import cartModel
from cars.models import carsModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def addToCart(request, product_id):
    product = get_object_or_404(carsModel, id=product_id)
    cart_item, created = cartModel.objects.get_or_create(
        user=request.user, product=product
    )

    if not created:
        cart_item.quantity += 1

        cart_item.save()

    product.quantity -= 1
    product.save()
    messages.success(request, f"{product.name} has been added to your profile.")

    return redirect("profile")
