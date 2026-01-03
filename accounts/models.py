from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('EMPLOYEE', 'Employee'),
    )

    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'employee_id']
