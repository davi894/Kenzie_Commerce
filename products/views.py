from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_reference"

    def get_object(self) -> Product:

        product = self.kwargs["product_reference"]

        product_id = Product.objects.get(pk=product)
        product_name = Product.objects.get(name=product)
        product_category = Product.objects.get(category=product)

        # if len(product_name) > 0:
        return product_name

        # else:
        #     return product_id
