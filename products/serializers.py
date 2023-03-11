from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        return ...

    def get_user(self, dict) -> dict:
        return {
            "email": dict.user.email,
        }

    def update(self, instance: Product, validated_data: dict) -> Product:

        instance.stock = validated_data.get("stock", instance.stock)

        instance.save()

        return instance

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "category",
            "price",
            "stock",
            "description",
            "user",
        ]

        depth = 1
       