from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated
from course.permissions import CoursePermissions,CourseRegistrationPermissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.models import Course,CourseRegistration
from course.serializers import CourseRegistrationSerializer, CourseRetrieveSerializer, CourseCreationSerializer

class CourseView(APIView):
    permission_classes = (CoursePermissions,)

    def get(self,request):
        queryset = Course.objects.all()
        return Response(status=status.HTTP_200_OK,data=CourseRetrieveSerializer(queryset,many=True).data)

    def post(self,request):
        serializer = CourseCreationSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            queryset = Course.objects.create(creator=request.user,**validated_data)
            return Response(status=status.HTTP_200_OK,data=CourseRetrieveSerializer(queryset).data)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.error_messages)

class RetrieveCourseView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
            return Response(status=status.HTTP_200_OK,data=CourseRetrieveSerializer(course).data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':'no such course exist'})


class CourseRegistrationView(APIView):
    permission_classes = (CourseRegistrationPermissions,)
    def post(self,request,pk):
        course = Course.objects.filter(pk=pk).first()
        if not course:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'No such course exists'})
        try:
            registration = CourseRegistration.objects.create(course=course,student=request.user)
            return Response(status=status.HTTP_201_CREATED,data=CourseRegistrationSerializer(registration).data)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':'duplicate'})
