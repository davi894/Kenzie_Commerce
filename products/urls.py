from django.urls import path, re_path
from . import views


urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/<int:product_reference>/", views.ProductsDetailView.as_view()),
    path("products/<str:product_reference>/", views.ProductsDetailView.as_view()),
    path("category/<str:category>/", views.ProductByCategoryView.as_view()),
]
