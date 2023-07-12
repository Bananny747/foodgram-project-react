from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя"""

    user = 'user'
    admin = 'admin'
    CHOICES = [
        (user, 'Аутентифицированный пользователь'),
        (admin, 'Администратор'),
    ]

    role = models.CharField(
        choices=CHOICES,
        default='user',
        max_length=16,
    )

    confirmation_code = models.CharField(
        max_length=32,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.is_superuser is True:
            self.role = self.admin
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.admin

    @property
    def is_user(self):
        return self.role == self.user


class Follow(models.Model):
    """Модель подписки на автора"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='follower',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='following'
    )

    class Meta:
        ordering = ('-id', )
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.user} подписан на {self.author}"
