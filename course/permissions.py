from rest_framework.permissions import IsAuthenticated


class CoursePermissions(IsAuthenticated):
    """Read and write access to educators and admins and read only access to students"""

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.method == 'POST':
                return bool(request.user.type=='Educator' or request.user.is_staff)
            return True
        return False

class CourseRegistrationPermissions(IsAuthenticated):
    """write access to students"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type=='Student')