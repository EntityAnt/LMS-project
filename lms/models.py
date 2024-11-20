from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="lms/previews", **NULLABLE, verbose_name="Превью"
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание курса",
        help_text="Введите краткое описание курса"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название урока")
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание курса",
        help_text="Введите краткое описание курса"
    )
    preview = models.ImageField(
        upload_to="lms/previews", **NULLABLE, verbose_name="Превью"
    )
    video_link = models.URLField(
        **NULLABLE, verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
