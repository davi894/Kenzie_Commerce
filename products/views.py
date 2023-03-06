from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_reference"

    def get_object(self) -> Product:
        product = self.kwargs["product_reference"]
        print(product, "_" * 100)

        my_list = [
            "Celulares",
            "Computadores",
            "Perifericos",
            "Eletronicos",
            "eletro",
        ]

        if product in my_list:
            product_obj = Product.objects.get(category=product)
            return product_obj

        if isinstance(product, int):
            product_id = Product.objects.get(pk=product)
            return product_id
        else:
            product_name = Product.objects.get(name=product)
            return product_name
