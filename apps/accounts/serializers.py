from rest_framework import serializers
from .models import User
from apps.patients.models import PatientProfile
from apps.doctors.models import DoctorProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.get('role', 'patient')
        user = User.objects.create_user(**validated_data)

        if role == 'patient':
            PatientProfile.objects.create(user=user)
        elif role == 'doctor':
            DoctorProfile.objects.create(user=user)

        return user
    