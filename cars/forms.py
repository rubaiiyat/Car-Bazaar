from django import forms
from .models import carsModel


class carsForm(forms.ModelForm):

    class Meta:
        model = carsModel
        fields = ["name", "content", "price", "quantity", "brand", "image"]
