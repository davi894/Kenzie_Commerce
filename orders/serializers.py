from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Orders, StatusChoices


class OrdersSerializer(serializers.ModelSerializer):

    status = serializers.ModelSerializer(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )

    def create(self, validated_data):
        ...

    class Meta:
        model = Orders

        fields = ["id", "status", "ordered_at", "user_id"]

        depth = 1
