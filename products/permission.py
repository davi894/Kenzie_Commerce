from rest_framework import permissions
import ipdb


class CreateProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        # ipdb.set_trace()

        return (
            request.user.is_superuser or request.user.employee
        ) and request.user.is_authenticated
