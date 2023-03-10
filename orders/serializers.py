from rest_framework import serializers
from .models import Orders, StatusChoices
from products.models import Product
from address.models import Address

from .models import Orders, StatusChoices
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from user.models import User

import ipdb


class OrdersSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)
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
        ...
        # return {
        #     "id": dict["address"].id,
        #     "street": dict["address"].street,
        #     "zip_code": dict["address"].zip_code,
        #     "state": dict["address"].state,
        #     "city": dict["address"].city,
        # }

    def create(self, validated_data):
        ...
        # status = validated_data["status"]
        # products = validated_data["products"]
        # address = validated_data["address"]
        # price = validated_data["products"].price
        # quantity = validated_data["quantity"]

        # order = Orders.objects.create(status=status, price=price, address_id=address.id)

        # orders_products = OrdersProducts.objects.create(
        #     quantity=quantity, product=products, order=order
        # )

        # stock_result = products.stock - quantity
        # setattr(products, "stock", stock_result)
        # products.save()

        # return {
        #     "id": order.id,
        #     "status": order.status,
        #     "ordered_at": order.ordered_at,
        #     "price": order.price * quantity,
        #     "address": order.address,
        #     "products": products.id,
        #     "quantity": orders_products.quantity,
        # }

    # def update(self, instance, validated_data):
    #     product = get_object_or_404(Product, id=validated_data["products"])
    #     orders_products = get_object_or_404(OrdersProducts, order=instance)
    #     setattr(instance, "status", validated_data["status"])
    #     instance.save()

    # product = get_object_or_404(Product, id=validated_data["products"])

    # orders_products = get_object_or_404(
    #     OrdersProducts, order=instance
    # )

    # setattr(instance, "status", validated_data["status"])

    # instance.save()

    # return {
    #     "id": instance.id,
    #     "status": instance.status,
    #     "ordered_at": instance.ordered_at,
    #     "price": instance.price * orders_products.quantity,
    #     "address": instance.address,
    #     "products": product.id,
    #     "quantity": orders_products.quantity,
    # }

    #     user = User.objects.get(pk=instance.address.user_id)

    #     ipdb.set_trace()

    #     send_mail(
    #         subject="Atualização de status de compra",
    #         message=f"O status da sua compra foi atualizado para {validated_data['status']}",
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[user.email],
    #         fail_silently=False,
    #     )

    #     return {
    #         "id": instance.id,
    #         "status": instance.status,
    #         "ordered_at": instance.ordered_at,
    #         "price": instance.price * orders_products.quantity,
    #         "address": instance.address,
    #         "products": product.id,
    #         "quantity": orders_products.quantity,
    #     }
