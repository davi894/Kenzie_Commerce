from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from .models import Cart
from .serializers import CartSerializer
import ipdb
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class CartView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
