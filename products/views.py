from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
<<<<<<< HEAD
from rest_framework.views import status
from rest_framework_simplejwt.authentication import JWTAuthentication
=======
>>>>>>> 7703d5906333721bd76046862895b54325ed1760
from .models import Product
from user.models import User
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
<<<<<<< HEAD
from rest_framework.response import Response
from .permission import CreateProductPermission
from user.models import User
=======
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import CreateProductPermission
>>>>>>> 7703d5906333721bd76046862895b54325ed1760


class ProductsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CreateProductPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)

        serializer.save(user=user)


class ProductByCategoryView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs["product_category"]
        queryset = Product.objects.filter(category=category)

        return queryset


class ProductByNameView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.kwargs["product_name"]
        queryset = Product.objects.filter(name=name)

        return queryset


class ProductsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CreateProductPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"

    def get_object(self) -> Product:
        product_reference = self.kwargs["product_id"]
        product = get_object_or_404(Product, pk=product_reference)

        return product
