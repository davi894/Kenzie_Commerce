from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ...

    def update(self, instance: User, validated_data: dict) -> User:
        ...

    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "password",
            "is_superuser",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ],
                "required": True,
            },
        }
