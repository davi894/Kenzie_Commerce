from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("user.urls")),
    path("api/", include("products.urls")),
    path("api/", include("address.urls")),
    path("api/", include("orders.urls")),
    path("api/", include("cart.urls")),
]
