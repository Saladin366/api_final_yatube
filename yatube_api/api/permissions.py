from rest_framework import permissions

YOU_CANNOT = 'У вас недостаточно прав для данного действия.'


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = YOU_CANNOT

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
