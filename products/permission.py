from rest_framework import permissions


class CreateProductPermission(permissions.BasePermission):
    def has_object_permission(self, request, vie, obj) -> bool:

        return (
            request.user.is_superuser or request.user.employee
        ) and request.user.is_authenticated
