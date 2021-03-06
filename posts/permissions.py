from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def hasObjectPermission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return object.author == request.user