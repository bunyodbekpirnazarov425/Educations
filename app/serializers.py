from rest_framework import serializers
from .models import Course, Lesson, Register

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.HyperlinkedRelatedField(
        many=True, view_name='lesson-detail', read_only=True)
    teacher = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = ['url', 'id', 'title', 'description', 'teacher', 'lessons']

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['url', 'id', 'title', 'content', 'course']

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ['url', 'id', 'student', 'course', 'date_enrolled']

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']