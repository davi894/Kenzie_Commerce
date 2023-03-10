from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import CreateProductPermission
from .permissions import IsAuthenticatedPermission
from .models import Orders
from .serializers import OrdersSerializer
from django.shortcuts import get_object_or_404
from products.models import Product
from address.models import Address
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from products.permissions import CreateProductPermission
import ipdb


class OrderViewGenerics(ListCreateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedPermission]
    serializer_class = OrdersSerializer

    def perform_create(self, serializer) -> Response:

        product = get_object_or_404(Product, id=self.request.data["products"])

        qtidade_pedida = serializer.validated_data["quantity"]

        if product.stock < qtidade_pedida:
            raise ServiceUnavailable()

        address = get_object_or_404(Address, id=self.request.data["address"])

        serializer.save(address=address, products=product)


class ServiceUnavailable(APIException):
    status_code = 400
    default_detail = "Estoque Insuficiente."
    default_code = "service_unavailable"


class OrderViewDetailGenerics(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateProductPermission]
    serializer_class = OrdersSerializer

    # def partial_update(self, serializer, pk):

    #     product = Product.objects.get(id=pk)

    #     ipdb.set_trace()

    #     return super().update(serializer, pk,)

    def perform_update(self, serializer):

        # order_id = self.kwargs["id"]
        product_id = self.kwargs["pk"]

        product = Product.objects.get(id=product_id)
        # orders = Orders.objects.get(id=order_id)

        serializer.save(products=product)
