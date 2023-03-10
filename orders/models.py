from django.db import models


class StatusChoices(models.TextChoices):
    DEFAULT = "Realizado"
    in_progress = "Em andamento"
    delivered = "Entregue"


class Orders(models.Model):
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )
    price = models.IntegerField()

    ordered_at = models.DateTimeField(auto_now_add=True)

    address = models.ForeignKey(
        "address.Address", on_delete=models.CASCADE, related_name="address"
    )

    products = models.ManyToManyField(
        "products.Product",
        through="OrdersProducts",
        related_name="products_cart",
    )


class OrdersProducts(models.Model):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="products_order"
    )
    order = models.ForeignKey(
        "orders.Orders", on_delete=models.CASCADE, related_name="order_products"
    )

    quantity = models.IntegerField()
