from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from apps.accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class CreatePatientProfileView(generics.CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user

        if user.role == "doctor":
            return Response({"detail": "Doctors are not allowed to create patient profiles."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Patient profile created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListPatientsView(generics.ListAPIView):
    queryset = PatientProfile.objects.filter(is_deleted=False).order_by('-id')
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrievePatientView(generics.RetrieveAPIView):
    queryset = PatientProfile.objects.filter(is_deleted=False)
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class SoftDeletePatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, id):
        patient = get_object_or_404(PatientProfile, id=id, is_deleted=False)

        if request.user.role == 'doctor':
            return Response({"detail": "Permission denied."}, status=403)

        patient.is_deleted = True
        patient.save()
        return Response({"detail": "Patient soft-deleted."}, status=200)