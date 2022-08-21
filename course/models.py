from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    image = models.URLField(max_length=500)
    creator = models.ForeignKey(User,related_name='course_created',on_delete=models.CASCADE)

class CourseRegistration(models.Model):
    class Meta:
        unique_together = (('student', 'course'),)
    student = models.ForeignKey(User,related_name='enrolled_courses',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name='enrollments',on_delete=models.CASCADE)