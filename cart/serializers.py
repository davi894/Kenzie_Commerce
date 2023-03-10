from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Cart
import ipdb
from orders.models import Orders
from address.models import Address
from products.models import Product
from user.models import User


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    products = serializers.ListField()
    value = serializers.IntegerField(read_only=True)
    # quantity = serializers.IntegerField(read_only=True)
    # user = serializers.SerializerMethodField()

    # def get_user(self, dict):
    #     return ...

    # {'products': [{'id': 1, 'quantity': 2}, {'id': 2, 'quantity': 4}], 'user': <User: Admin>}

    def create(self, validated_data):
        # ipdb.set_trace()
        # Cart.objects.create(user=validated_data["user"])
        total_price = 0
        products = []
        for item in validated_data["products"]:
            product = Product.objects.get(pk=item["id"])
            product_price = product.price * item["quantity"]
            product_stock = product.stock
            stock_result = product_stock - item["quantity"]
            setattr(product, "stock", stock_result)
            product.save()
            total_price += product_price
            employee = User.objects.get(pk=product.user.id)

            products.append(
                {
                    "name": product.name,
                    "price": product.price,
                    "quantity": item["quantity"],
                    "employee_email": employee.email,
                }
            )
        Cart.objects.create(
            value=total_price, user=validated_data["user"], products=products
        )

        # print(products, "-" * 100)

        return ...

    # def create(self, validated_data):
    #     user = validated_data["user"]
    #     user_address = Address.objects.get(user=user)
    #     user_order = Orders.objects.filter(address=user_address)
    #     total_value = 0
    #     products_infos = []
    #     for item in user_order.values():
    #         total_value += item["price"]
    #         orders_products = OrdersProducts.objects.get(pk=item["id"])
    #         product = Product.objects.get(pk=orders_products.product_id)
    #         products_infos.append(
    #             {
    #                 "name": product.name,
    #                 "price": product.price,
    #             }
    #         )
    #     print(products_infos, "-" * 100)
    #     # ipdb.set_trace()

    #     return
