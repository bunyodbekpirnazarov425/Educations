from django.urls import path, include
from rest_framework import routers
from .views import (CourseListCreateView,
                    CourseDetailView,
                    LessonListCreateView,
                    LessonDetailView,
                    RegisterListCreateView,
                    RegisterDetailView)


urlpatterns = [
    # path('', include(router.urls)),
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('enrollments/', RegisterListCreateView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', RegisterDetailView.as_view(), name='enrollment-detail'),
]
