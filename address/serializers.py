from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, dict):
        return {
            "email": dict.user.email,
            "username": dict.user.username,
            "id": dict.user.id,
        }

    class Meta:

        model = Address

        fields = [
            "id",
            "zip_code",
            "street",
            "number",
            "city",
            "state",
            "user",
        ]

        depth = 1
