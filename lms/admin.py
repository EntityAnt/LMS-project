from django.contrib import admin

from lms.models import Course, Lesson
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "tg_nick", "city", "avatar")
    list_filter = ("email",)
    search_fields = ("email",)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "paid_course", "paid_lesson", "amount", "payment_method")
    list_filter = ("date",)
    search_fields = ("user", "paid_course", "paid_lesson")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "description")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "description", "video_link", "course")
    list_filter = ("name",)
    search_fields = ("name", "description")
