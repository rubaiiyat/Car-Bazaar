from django.contrib import admin
from .models import carsModel, commentModel

# Register your models here.
admin.site.register(carsModel)
admin.site.register(commentModel)
