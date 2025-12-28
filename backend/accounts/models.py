from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STAFF = 'STAFF'
    STUDENT = 'STUDENT'

    ROLE_CHOICES =[
        (STAFF, 'Fcaulty/Staff'),
        (STUDENT, 'Student'),
    ]

    role=models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STAFF
    )

def __str__(self):
    return self.username