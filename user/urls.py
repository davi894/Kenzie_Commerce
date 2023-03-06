from django.urls import path
from .views import UserViewGenerics, LoginJWTView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("user/", UserViewGenerics.as_view()),
    path("user/login/", LoginJWTView.as_view()),
    path("user/login/refresh/", TokenRefreshView.as_view()),
]
