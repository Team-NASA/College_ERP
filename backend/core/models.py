from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    code=models.CharField(max_length=20, unique=True)
    name=models.CharField(max_length=100)
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    def __str__(self):
        return self.name