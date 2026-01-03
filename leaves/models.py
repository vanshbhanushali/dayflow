from django.db import models
from django.conf import settings

class LeaveRequest(models.Model):
    LEAVE_TYPE = (
        ('Paid', 'Paid'),
        ('Sick', 'Sick'),
        ('Unpaid', 'Unpaid'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    def __str__(self):
        return f"{self.user.email} - {self.status}"
