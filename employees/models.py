from django.db import models
from django.conf import settings

class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.email
