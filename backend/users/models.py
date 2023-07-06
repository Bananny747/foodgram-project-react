from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель из yamdb, требует подстройки
class User(AbstractUser):
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
