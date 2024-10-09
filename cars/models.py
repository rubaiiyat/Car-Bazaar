from django.db import models
from brand.models import brandModel


# Create your models here.
class carsModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    brand = models.ForeignKey(brandModel, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="cars/uploads",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.brand} - ${self.price}"


class commentModel(models.Model):
    post = models.ForeignKey(
        carsModel, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.comment}"
