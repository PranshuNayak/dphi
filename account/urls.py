from django.urls import path,include
from . import views

urlpatterns = [
    path('courses/',views.ListEnrolledCourseView.as_view()),
    path('<int:pk>/enrollments/',views.ListEnrolledUserView.as_view())
]