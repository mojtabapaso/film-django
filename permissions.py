from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerProfile(BasePermission):
    message = "این پروفایل شما نیست "

    def has_object_permission(self, request, view, obj):
        if SAFE_METHODS:
            return False
        return obj.user == request.user
