from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .permission import CreateProductPermission
from user.models import User
import ipdb


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateProductPermission]
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)

        serializer.save(user=user)


class ProductByCategoryView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = Product.objects.filter(category=category)

        return queryset


class ProductsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_reference"

    def get_object(self) -> Product:
        product_reference = self.kwargs["product_reference"]

        if isinstance(product_reference, int):
            product = get_object_or_404(Product, pk=product_reference)
            return product
        else:
            product = get_object_or_404(Product, name=product_reference)
            return product
