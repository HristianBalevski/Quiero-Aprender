from rest_framework.permissions import BasePermission

class CanSeeApiPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Teachers').exists()