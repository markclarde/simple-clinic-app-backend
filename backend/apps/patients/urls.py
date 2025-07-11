from django.urls import path
from .views import CreatePatientProfileView

urlpatterns = [
    path('create/', CreatePatientProfileView.as_view(), name='create-patient-profile'),
]
