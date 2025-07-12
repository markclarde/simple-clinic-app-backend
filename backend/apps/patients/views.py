from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from apps.accounts.models import User

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
    queryset = PatientProfile.objects.all().order_by('-id')
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrievePatientView(generics.RetrieveAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'