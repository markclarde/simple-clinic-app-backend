from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = None
    last_name = None

    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return f"{self.username} ({self.role})"
    