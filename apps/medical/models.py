from django.db import models
from apps.accounts.models import User
from apps.appointments.models import Appointment

class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Record for {self.appointment.patient.username} by {self.doctor.username}"
