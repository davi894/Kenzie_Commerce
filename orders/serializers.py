from cart.models import Cart, ProductsInCart
from .models import Orders, StatusChoices
from rest_framework import serializers
from django.conf import settings
from products.models import Product
from django.core.mail import send_mail
import ipdb


class OrdersSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)
    status = serializers.ChoiceField(
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )
    ordered_at = serializers.DateTimeField(read_only=True)
    address = serializers.SerializerMethodField()
    cart = serializers.SerializerMethodField()

    def get_address(self, dict):
        return {
            "id": dict["address"].id,
            "street": dict["address"].street,
            "zip_code": dict["address"].zip_code,
            "state": dict["address"].state,
            "city": dict["address"].city,
            "user_email": dict["address"].user.email,
        }

    def get_cart(self, dict):
        list_products = []

        for products in dict["cart"]:
            employee_product = Product.objects.get(id=products["product_id"])
            products["employee_email"] = employee_product.user.email
            list_products.append(products)

        return list_products

    def create(self, validated_data):
        user = validated_data["address"].user
        address = validated_data["address"]
        cart_user = Cart.objects.get(user=user)
        producst_in_cart = ProductsInCart.objects.filter(cart=cart_user.id)

        order = Orders.objects.create(
            cart=cart_user, price=cart_user.value, address=address
        )

        return {
            "id": order.id,
            "status": order.status,
            "address": address,
            "ordered_at": order.ordered_at,
            "cart": producst_in_cart.values(),
        }

    def update(self, instance, validated_data):

        setattr(instance, "status", validated_data["status"])
        instance.save()
        send_mail(
            subject="Atualização de status de compra",
            message=f"O status da sua compra foi atualizado para {validated_data['status']}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.address.user.email],
            fail_silently=False,
        )

        producst_in_cart = ProductsInCart.objects.filter(cart=instance.cart.id)
        
        return {
            "id": instance.id,
            "status": instance.status,
            "address": instance.address,
            "ordered_at": instance.ordered_at,
            "cart": producst_in_cart.values(),
        }
        # product = get_object_or_404(Product, id=validated_data["products"])
        # orders_products = get_object_or_404(OrdersProducts, order=instance)
        # setattr(instance, "status", validated_data["status"])
        # instance.save()

        # product = get_object_or_404(Product, id=validated_data["products"])

        # orders_products = get_object_or_404(OrdersProducts, order=instance)

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
        ###################################################
        # user = User.objects.get(pk=instance.address.user_id)

        # ipdb.set_trace()

        # return {
        #     "id": instance.id,
        #     "status": instance.status,
        #     "ordered_at": instance.ordered_at,
        #     "price": instance.price * orders_products.quantity,
        #     "address": instance.address,
        #     "products": product.id,
        #     "quantity": orders_products.quantity,
        # }
        ...
