from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsConsultantPermission(permissions.BasePermission):
    message = 'User is not consultant.'

    def has_permission(self, request, view):
        if request.method == "OPTIONS":
            return True

        # User is authenticated
        if not (request.user and request.user.is_authenticated):
            return False

        # User is consultant
        if request.user.is_authenticated and request.user.is_consultant():
            return True
        return False


class IsConsultantUnsafePermission(permissions.BasePermission):
    message = 'User should be consultant.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not (request.user and request.user.is_authenticated):
            return False

        else:
            if request.user.is_authenticated and request.user.is_consultant():
                return True
            return False


class CustomIsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == "OPTIONS":
            return True
        return super().has_permission(request, view)
