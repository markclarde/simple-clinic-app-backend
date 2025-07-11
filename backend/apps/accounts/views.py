from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "User registered successfully", "user": serializer.data},
            status=status.HTTP_201_CREATED
        )
