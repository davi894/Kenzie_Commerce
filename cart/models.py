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
        through="cart.ProductsInCart",
        related_name="products",
    )


class ProductsInCart(models.Model):
    quantity = models.IntegerField()

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="products_carts"
    )
    cart = models.ForeignKey(
        "cart.Cart", on_delete=models.CASCADE, related_name="cart_products"
    )
