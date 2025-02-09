from django.contrib.auth import get_user_model
from django.db import models

from .constants import MAX_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст', help_text='Текст поста')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группы',
        help_text='Группа, к которой будет относиться пост'
    )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/post/{self.pk}'

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
        ordering = ['-pub_date']
