from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=127)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=127)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="address"
    )
