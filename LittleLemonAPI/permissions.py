from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True

class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='delivery crew').exists():
            return True
