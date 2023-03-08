from rest_framework.views import Request, View
from rest_framework import permissions
<<<<<<< HEAD
import ipdb
=======
from .models import Product
>>>>>>> 7703d5906333721bd76046862895b54325ed1760


class CreateProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
<<<<<<< HEAD

        # ipdb.set_trace()

=======
        # ipdb.set_trace()
>>>>>>> 7703d5906333721bd76046862895b54325ed1760
        return (
            request.user.is_superuser or request.user.employee
        ) and request.user.is_authenticated
