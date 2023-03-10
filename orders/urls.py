from django.urls import path
from .views import OrderViewGenerics, OrderViewDetailGenerics

urlpatterns = [
    path("orders/", OrderViewGenerics.as_view()),
    path("orders/<int:pk>/", OrderViewDetailGenerics.as_view()),
]
