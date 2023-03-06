from django.urls import path, re_path
from . import views


urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/<product_reference>/", views.ProductsDetailView.as_view()),
]
