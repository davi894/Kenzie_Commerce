from rest_framework import permissions


class CreateProductPermission(permissions.BasePermission):
    def has_object_permission(self, request, vie, obj) -> bool:
        if request.user.is_superuser and request.user.is_authenticated:
            return True

        if request.user.employee and request.user.is_authenticated:
            return True

        return False
