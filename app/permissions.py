from rest_framework.permissions import BasePermission

class IsTeacherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.teacher == request.user
