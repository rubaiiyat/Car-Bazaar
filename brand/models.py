from django.db import models


# Create your models here.
class brandModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
