from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите почту')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Телефон', help_text='Укажите номер телефона')
    tg_nick = models.CharField(max_length=50, **NULLABLE, verbose_name='ТГ-ник', help_text='Укажите ТГ ник')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город', help_text='Укажите город')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='Аватар',
                               help_text='Загрузите фото аватара')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

