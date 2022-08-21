from rest_framework.permissions import IsAdminUser
from course.models import Course
from django.core.exceptions import ObjectDoesNotExist
class isAdminOrCourseOwner(IsAdminUser):
    def has_permission(self, request, view):
        if request.user:
            try:
                course = Course.objects.get(id=view.kwargs.get('pk', None))
                if request.user.is_staff or (course.creator == request.user):
                    return True
                return False
            except ObjectDoesNotExist:
                return False
        return False
