from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_of_lessons = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()

    def get_count_of_lessons(self, obj):
        # Подсчет количества уроков, связанных с данным курсом

        return obj.lessons.count()

    def get_lessons_info(self, obj):
        # Получение информации об уроках, связанных с данным курсом

        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = ("id", "name", "description", "count_of_lessons", "lessons_info")
