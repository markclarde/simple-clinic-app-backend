from django.db import models
from apps.accounts.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient: {self.user.username}"
