from django.contrib.auth.models import AbstractUser
from django.db import models

from posts.constants import MAX_LENGTH


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username', 'first_name', 'last_name'
    ]
    username = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name='Логин'
    )
    email = models.EmailField(
        max_length=MAX_LENGTH,
        verbose_name='Адрес электронной почты',
        unique=True
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Фамилия'
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'