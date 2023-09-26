from django.contrib import admin
from .models import Patient, MedicalHistory, Appointment
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'name', 'date_of_birth', 'gender', 'contact_information', 'entry_date', 'entry_name']


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
	list_display = ['patient', 'allergies', 'medications', 'previous_illnesses', 'surgeries', 'diagnosis_date', 'diagnosed_by']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment_date', 'appointment_time', 'additional_notes', 'appointment_doctor']