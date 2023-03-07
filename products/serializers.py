from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, dict):
        return {
            "email": dict.user.email,
            "username": dict.user.username,
            "id": dict.user.id,
        }

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
       