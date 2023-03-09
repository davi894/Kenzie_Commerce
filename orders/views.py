from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import CreateProductPermission
from .permissions import IsAuthenticatedPermission
from .models import Orders
from .serializers import OrdersSerializer
from django.shortcuts import get_object_or_404
from products.models import Product
from address.models import Address
import ipdb


class OrderViewGenerics(ListCreateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedPermission]
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):

        product = get_object_or_404(Product, id=self.request.data["products"])
        address = get_object_or_404(Address, id=self.request.data["address"])

        serializer.save(address=address, products=product)


class OrderViewDetailGenerics(CreateAPIView):
    ...
