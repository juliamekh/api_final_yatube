from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class OnlyAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class GroupOnlyGet(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        raise PermissionDenied()