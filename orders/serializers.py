from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Orders, StatusChoices, OrdersProducts
from django.shortcuts import get_object_or_404
from products.models import Product
from address.models import Address

import ipdb


class OrdersSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )
    ordered_at = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    products = serializers.IntegerField()
    address = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()

    def get_address(self, dict):
        return {
            "id": dict["address"].id,
            "street": dict["address"].street,
            "zip_code": dict["address"].zip_code,
            "state": dict["address"].state,
            "city": dict["address"].city,
        }

    def create(self, validated_data):
        status = validated_data["status"]
        products = validated_data["products"]
        address = validated_data["address"]
        price = validated_data["products"].price
        quantity = validated_data["quantity"]

        order = Orders.objects.create(status=status, price=price, address_id=address.id)

        orders_products = OrdersProducts.objects.create(
            quantity=quantity, product=products, order=order
        )

        stock_result = products.stock - quantity
        setattr(products, "stock", stock_result)
        products.save()

        return {
            "id": order.id,
            "status": order.status,
            "ordered_at": order.ordered_at,
            "price": order.price * quantity,
            "address": order.address,
            "products": products.id,
            "quantity": orders_products.quantity,
        }

    def update(self, instance, validated_data):

        setattr(instance, "status", validated_data["status"])
        instance.save()

        ipdb.set_trace()
        return instance
