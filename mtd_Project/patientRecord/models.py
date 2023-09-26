from django.db import models
from django.utils import timezone


# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_information = models.CharField(max_length=11)
    entry_date = models.DateField(default=timezone.now)
    entry_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.date_of_birth}, {self.contact_information} "


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergies = models.CharField(max_length=255, blank=True, null=True)
    medications = models.CharField(max_length=255, blank=True, null=True)
    previous_illnesses = models.CharField(max_length=255, blank=True, null=True)
    surgeries = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_note = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_date = models.DateField(default=timezone.now)
    diagnosed_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient.name}, {self.patient.contact_information}, {self.diagnosis_note}, {self.diagnosis_date}, {self.diagnosed_by}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    additional_notes = models.CharField(max_length=255, blank=True, null=True)
    appointment_doctor = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient.name}, {self.patient.contact_information}, {self.appointment_date}"