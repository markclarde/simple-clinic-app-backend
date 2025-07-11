from django.urls import path
from .views import MedicalRecordView

urlpatterns = [
    path('', MedicalRecordView.as_view(), name='medical-records'),
]
