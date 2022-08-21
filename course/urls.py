from django.urls import path
from . import views
urlpatterns = [
    path('',views.CourseView.as_view()),
    path('<int:pk>/',views.RetrieveCourseView.as_view()),
    path('<int:pk>/register/',views.CourseRegistrationView.as_view())
]