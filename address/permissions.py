from rest_framework import permissions
import ipdb


class RegisterAddressPermission(permissions.BasePermission):
    def has_object_permission(self, request, vie, obj) -> bool:
        ipdb.set_trace()
        return request.user and request.user.is_authenticated
