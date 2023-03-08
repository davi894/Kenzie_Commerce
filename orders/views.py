from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permission import CreateProductPermission
from .models import Orders
from .serializers import OrdersSerializer
from django.shortcuts import get_object_or_404
from user.models import User
from address.models import Address


class OrderViewGenerics(ListCreateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateProductPermission]
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):

        serializer.save(address=self.request.user.address)


class OrderViewDetailGenerics(CreateAPIView):
    ...
