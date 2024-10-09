from django import forms
from .models import carsModel, commentModel


class carsForm(forms.ModelForm):

    class Meta:
        model = carsModel
        fields = ["name", "content", "price", "quantity", "brand", "image"]


class commentForm(forms.ModelForm):
    class Meta:
        model = commentModel
        fields = ["name", "comment"]
