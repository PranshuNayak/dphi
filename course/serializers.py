from rest_framework.serializers import ModelSerializer
from course.models import Course, CourseRegistration

class CourseCreationSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','description','image']

class CourseRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','description','image','creator']

class CourseRegistrationSerializer(ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = ['id','student','course']