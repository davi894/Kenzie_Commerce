from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ...

    class Meta:
        model = Cart

        fields = ["id", "value", "user_id", "products_id"]

        depth = 2
