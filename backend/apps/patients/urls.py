from django.urls import path
from .views import CreatePatientProfileView, ListPatientsView, RetrievePatientView

urlpatterns = [
    path('create/', CreatePatientProfileView.as_view(), name='create-patient-profile'),
    path('', ListPatientsView.as_view(), name='list-patients'),
    path('<int:id>/', RetrievePatientView.as_view(), name='get-patient'),
]
