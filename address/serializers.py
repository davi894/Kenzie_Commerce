from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ...

    class Meta:

        model = Address

        fields = [
            "id",
            "zip_code",
            "street",
            "number",
            "city",
            "state",
            "user_id",
        ]

        depth = 1
