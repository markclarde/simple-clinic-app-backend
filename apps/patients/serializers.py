from rest_framework import serializers
from .models import PatientProfile

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'birth_date', 'gender', 'contact_number', 'address']
        extra_kwargs = {
            'user': {'read_only': True}
        }
