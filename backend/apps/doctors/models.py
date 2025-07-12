from django.db import models
from apps.accounts.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    license_no = models.CharField(max_length=50, blank=True, null=True)
    years_experience = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.user.username}"