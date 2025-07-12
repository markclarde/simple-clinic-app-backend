from django.urls import path
from .views import CreatePatientProfileView, ListPatientsView, RetrievePatientView, SoftDeletePatientView

urlpatterns = [
    path('create/', CreatePatientProfileView.as_view(), name='create-patient-profile'),
    path('', ListPatientsView.as_view(), name='list-patients'),
    path('<int:id>/', RetrievePatientView.as_view(), name='get-patient'),
    path('<int:id>/delete/', SoftDeletePatientView.as_view(), name='soft-delete-patient'),
]
