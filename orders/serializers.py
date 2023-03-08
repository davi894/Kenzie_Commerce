from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Orders, StatusChoices
import ipdb


class OrdersSerializer(serializers.ModelSerializer):

    status = serializers.ChoiceField(
        # max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )

    def create(self, validated_data):
        ipdb.set_trace()

    class Meta:
        model = Orders

        fields = [
            "id",
            "status",
            "ordered_at",
            "price",
            "address",
            "products",
        ]

        depth = 1
