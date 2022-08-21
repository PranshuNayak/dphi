from account.permissions import isAdminOrCourseOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from course.models import Course
from course.serializers import CourseRegistrationSerializer
from rest_framework.response import Response

from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class ListEnrolledCourseView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        queryset = User.objects.get(id=request.user.id).enrolled_courses
        return Response(status=status.HTTP_200_OK,data=CourseRegistrationSerializer(queryset,many=True).data)

class ListEnrolledUserView(APIView):
    permission_classes = (isAdminOrCourseOwner,)
    def get(self,request,pk):
        queryset = Course.objects.get(pk=pk).enrollments
        return Response(status=status.HTTP_200_OK,data=CourseRegistrationSerializer(queryset,many=True).data)

