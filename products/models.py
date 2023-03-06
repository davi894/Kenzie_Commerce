from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    category = models.CharField(max_length=127)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="products"
    )
