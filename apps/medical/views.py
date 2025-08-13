from rest_framework import generics
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class MedicalRecordView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
