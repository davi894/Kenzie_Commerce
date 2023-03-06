from django.db import models


class Cart(models.Model):
    value = models.IntegerField()

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="cart",
    )

    products = models.ManyToManyField(
        "products.Product",
        related_name="products_cart",
    )
