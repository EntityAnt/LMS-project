from django.db import models



NULLABLE = {"blank": True, "null": True}


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

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название урока")
    description = models.TextField(
        **NULLABLE,
        verbose_name="Описание курса",
        help_text="Введите краткое описание урока"
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

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
