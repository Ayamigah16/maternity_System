from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

from .models import Patient, Doctors, Appointments, Billings, Medical_Records, Obstetric_care, Neonatal_care
from django.views.generic.edit import CreateView, UpdateView, DeleteView        # to create an instance of a table;  to update a particluar instance of the table in a database
from django.views.generic.list import ListView   # to display multiple instances of a table in a databases
from django.views.generic.detail import DetailView  # to display specific instance of a table in a database     

from django.urls import reverse_lazy, reverse
# Create your views here.
    
# Patient views
class PatientCreateView(CreateView):
    model = Patient
    fields = ['patient_id', 'patient_name', 'patient_contact', 'med_history']
    template_name = 'webviews/patient_create.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'webviews/patient_detail.html'

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['patient_name', 'patient_contact', 'med_history']
    template_name = 'webviews/patient_update.html'

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('webviews:patient_list')
    template_name = 'webviews/patient_delete.html'

# Doctor views
class DoctorCreateView(CreateView):
    model = Doctors
    fields = ['doctor_id', 'doc_name', 'contact', 'speciality']
    template_name = 'webviews/doctor_create.html'

class DoctorDetailView(DetailView):
    model = Doctors
    template_name = 'webviews/doctor_detail.html'

class DoctorUpdateView(UpdateView):
    model = Doctors
    fields = ['doc_name', 'contact', 'speciality']
    template_name = 'webviews/doctor_update.html'

class DoctorDeleteView(DeleteView):
    model = Doctors
    success_url = reverse_lazy('doctor_list')
    template_name = 'webviews/doctor_delete.html'


# Appointment views
class AppointmentCreateView(CreateView):
    model = Appointments
    fields = ['appointment_id', 'appointment_date', 'doctor_id', 'patient_id']
    template_name = 'webviews/appointment_create.html'

class AppointmentDetailView(DetailView):
    model = Appointments
    template_name = 'webviews/appointment_detail.html'

class AppointmentUpdateView(UpdateView):
    model = Appointments
    fields = ['appointment_date', 'doctor_id', 'patient_id']
    template_name = 'webviews/appointment_update.html'

class AppointmentDeleteView(DeleteView):
    model = Appointments
    success_url = reverse_lazy('webviews:appointment_list')
    template_name = 'webviews/appointment_delete.html'


# Medical records views
class MedicalRecordCreateView(CreateView):
    model = Medical_Records
    fields = ['patient_id', 'diagnosis', 'treatment_plan', 'medication']
    template_name = 'webviews/medical_record_create.html'

class MedicalRecordDetailView(DetailView):
    model = Medical_Records
    template_name = 'webviews/medical_record_detail.html'

class MedicalRecordUpdateView(UpdateView):
    model = Medical_Records
    fields = ['diagnosis', 'treatment_plan', 'medication']
    template_name = 'webviews/medical_record_update.html'

class MedicalRecordDeleteView(DeleteView):
    model = Medical_Records
    success_url = reverse_lazy('webviews:medical_record_list')
    template_name = 'webviews/medical_record_delete.html'


# Obstetric care views
class ObstetricCareCreateView(CreateView):
    model = Obstetric_care
    fields = ['patient_id', 'admission_date', 'delivery_date', 'medi_interventions']
    template_name = 'webviews/obstetric_care_create.html'

class ObstetricCareDetailView(DetailView):
    model = Obstetric_care
    template_name = 'webviews/obstetric_care_detail.html'

class ObstetricCareUpdateView(UpdateView):
    model = Obstetric_care
    fields = ['admission_date', 'delivery_date', 'medi_interv']
    template_name = 'webviews/obstetric_care_update.html'

class ObstetricCareDeleteView(DeleteView):
    model = Obstetric_care
    success_url = reverse_lazy('webviews:obstetric_care_list')
    template_name = 'webviews/obstetric_care__delete.html'
    
# Neonatal Care views
class NeonatalCareCreateView(CreateView):
    model = Neonatal_care
    fields = ['baby_id', 'birth_date', 'weight', 'length']
    template_name = 'webviews/neonatal_care_create.html'

class NeonatalCareDetailView(DetailView):
    model = Neonatal_care
    template_name = 'webviews/neonatal_care_detail.html'

class NeonatalCareUpdateView(UpdateView):
    model = Neonatal_care
    fields = ['baby_id', 'birth_date', 'weight', 'length']
    template_name = 'webviews/neonatal_care_update.html'

class NeonatalCareDeleteView(DeleteView):
    model =  Neonatal_care
    success_url = reverse_lazy('webviews:neonatal_care_list')
    template_name = 'webviews/neonatal_care_delete.html'
    
# Billings views
class BillingsCreateView(CreateView):
    model = Billings
    fields = ['patient_id', 'amount_owned', 'amount_paid', 'insurance_info', 'payment_date']
    template_name = 'webviews/billings_create.html'

class BillingsDetailView(DetailView):
    model = Billings
    template_name = 'webviews/billings_detail.html'

class BillingsUpdateView(UpdateView):
    model = Billings
    fields = ['patient_id', 'amount_owned', 'amount_paid', 'insurance_info', 'payment_date']
    template_name = 'webviews/billings_update.html'

class BillingsDeleteView(DeleteView):
    model = Billings
    success_url = reverse_lazy('webviews:medical_record_list')
    template_name = 'webviews/billings_delete.html'
