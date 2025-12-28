from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Department, Subject


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

    subject=models.ManyToManyField(
        Subject,
        blank=True,
        related_name='faculties'
    )

    def __str__(self):
        return self.username