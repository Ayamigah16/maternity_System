from django.urls import path

from .views import ( 
    PatientCreateView, 
    PatientDetailView, 
    PatientUpdateView, 
    PatientDeleteView, 
    DoctorCreateView, 
    DoctorDetailView, 
    DoctorUpdateView, 
    DoctorDeleteView,
    AppointmentCreateView, 
    AppointmentDetailView, 
    AppointmentUpdateView, 
    AppointmentDeleteView, 
    MedicalRecordCreateView, 
    MedicalRecordDetailView, 
    MedicalRecordUpdateView, 
    MedicalRecordDeleteView, 
    ObstetricCareCreateView, 
    ObstetricCareDetailView, 
    ObstetricCareUpdateView, 
    ObstetricCareDeleteView, 
    NeonatalCareCreateView, 
    NeonatalCareDetailView, 
    NeonatalCareUpdateView, 
    NeonatalCareDeleteView, 
    BillingsCreateView, 
    BillingsDetailView, 
    BillingsUpdateView, 
    BillingsDeleteView,
)
app_name = "crudapp"
urlpatterns = [
    # Patient urls
    path('patient/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    
    # Doctor urls
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor-delete'),
    
    # Appointment urls
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    
    # Medical Record urls
    path('medical-record/create/', MedicalRecordCreateView.as_view(), name='medical-record-create'),
    path('medical-record/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('medical-record/<int:pk>/update/', MedicalRecordUpdateView.as_view(), name='medical-record-update'),
    path('medical-record/<int:pk>/delete/', MedicalRecordDeleteView.as_view(), name='medical-record-delete'),
    
    # Obstetric Care urls
    path('obstetric-care/create/', ObstetricCareCreateView.as_view(), name='obstetric-care-create'),
    path('obstetric-care/<int:pk>/', ObstetricCareDetailView.as_view(), name='obstetric-care-detail'),
    path('obstetric-care/<int:pk>/update/', ObstetricCareUpdateView.as_view(), name='obstetric-care-update'),
    path('obstetric-care/<int:pk>/delete/', ObstetricCareDeleteView.as_view(), name='obstetric-care-delete'),
    
    # Neonatal Care urls
    path('neonatal-care/create/', NeonatalCareCreateView.as_view(), name='neonatal-care-create'),
    path('neonatal-care/<int:pk>/', NeonatalCareDetailView.as_view(), name='neonatal-care-detail'),
    path('neonatal-care/<int:pk>/update/', NeonatalCareUpdateView.as_view(), name='neonatal-care-update'),
    path('neonatal-care/<int:pk>/delete/', NeonatalCareDeleteView.as_view(), name="neonatal-care-delete"),
    
    # Billings urls
    path('billings/create/', BillingsCreateView.as_view(), name='billings-create'),
    path('billings/<int:pk>/', BillingsDetailView.as_view(), name='billings-detail'),
    path('billings/<int:pk>/update/', BillingsUpdateView.as_view(), name='billings-update'),
    path('billings/<int:pk>/delete/', BillingsDeleteView.as_view(), name="billings-delete"),
]