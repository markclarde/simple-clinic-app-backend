from django.db import models
from apps.accounts.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=10,
        choices=[("pending", "Pending"), ("approved", "Approved"), ("done", "Done")],
        default="pending"
    )

    def __str__(self):
        return f"{self.patient.username} → {self.doctor.username} on {self.date}"
