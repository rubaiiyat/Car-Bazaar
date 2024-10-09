from django.db import models
from django.contrib.auth.models import User
from cars.models import carsModel


class cartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(carsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"({self.user.username}- {self.user.email}) - {self.product.name} - {self.quantity}"
