from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework.generics import CreateAPIView
from .models import User


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserViewGenerics(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
