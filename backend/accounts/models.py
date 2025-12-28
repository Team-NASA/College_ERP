from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Department


class User(AbstractUser):
    STAFF = 'STAFF'
    STUDENT = 'STUDENT'

    ROLE_CHOICES = [
        (STAFF, 'Faculty / Staff'),
        (STUDENT, 'Student'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STAFF
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username