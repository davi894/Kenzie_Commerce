from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     ...

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "category",
            "price",
            "stock",
            "description",
            "user_id",
        ]

        depth = 1
