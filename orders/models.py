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

    ordered_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="owner"
    )
