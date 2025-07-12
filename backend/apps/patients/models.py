from django.db import models
from apps.accounts.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
