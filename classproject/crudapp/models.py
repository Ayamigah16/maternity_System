from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True, unique=True)
    patient_name = models.CharField(max_length=50)
    patient_contact = models.CharField(max_length=200)
    med_history = models.CharField(max_length=200)
    
    class Meta:
        db_table = "patient"
        
    def __str__(self):
        patientId = "Patient_ID : " + str(self.patient_id)
        patientName = "Patient_Name : " + self.patient_name
        return "%s %s" % (patientId, patientName)  


class Doctors(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    speciality = models.CharField(max_length=50)
    
    class Meta:
        db_table = "doctor"
      

class Appointments(models.Model):
    appointment_id = models.IntegerField(primary_key=True, unique=True)
    appointment_date = models.DateTimeField() 
    doctor_id = models.ForeignKey(
        Doctors, related_name="docToMeet",to_field="doctor_id", on_delete=models.CASCADE
    ) 
    patient_id = models.ForeignKey(
        Patient, related_name="appointment",to_field="patient_id", on_delete=models.CASCADE
    )
    
    class Meta:
        db_table = "appointments"
    
    def __str__(self):
        appointmentDate = "Appointment_Date : " + str(self.appointment_date)
        docId = "Doctor_Id : " + str(self.doctor_id)
        return "%s %s" % (appointmentDate, docId)  
    
    
class Medical_Records(models.Model):
    patient_id = models.ForeignKey(
        Patient, related_name="medicals",to_field="patient_id", on_delete=models.CASCADE
    )
    diagnosis = models.CharField(max_length=200)
    treatment_plan = models.CharField(max_length=200)
    medication = models.CharField(max_length=200)
    
    class Meta:
        db_table = "medical_records"
    
class Obstetric_care(models.Model):
    patient_id = models.ForeignKey(
        Patient, related_name="obs_care",to_field="patient_id", on_delete=models.CASCADE
    )
    admission_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    medi_interventions = models.CharField(max_length=200)
    
    class Meta:
        db_table = "obstetric_care"

class Neonatal_care(models.Model):
    baby_id = models.IntegerField(primary_key=True)
    birth_date = models.DateTimeField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    length = models.DecimalField(decimal_places=2, max_digits=5)
        
    class Meta:
        db_table = "neonatal_care"

class Billings(models.Model):
    patient_id = models.ForeignKey(
        Patient, related_name="bills",to_field="patient_id", on_delete=models.CASCADE
    )
    amount_owned = models.DecimalField(max_digits=5, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=5, decimal_places=2) 
    insurance_info = models.CharField(max_length=200)
    payment_date = models.DateTimeField()
    
    class Meta:
        db_table = "billings"