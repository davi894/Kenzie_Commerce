from django.urls import path
from .views import OrderViewGenerics, OrderViewDetailGenerics

urlpatterns = [
    path("order/", OrderViewGenerics.as_view()),
    path("order/products/<int:id>/", OrderViewDetailGenerics.as_view()),
]
