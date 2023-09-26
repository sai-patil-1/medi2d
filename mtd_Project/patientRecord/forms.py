from typing import Any
from django import forms
from .models import Patient, MedicalHistory, Appointment
from django.forms.widgets import DateInput, Select
from django.db.models import Q
from datetime import date, datetime


class PatientForm_Edit(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "date_of_birth", "gender", "contact_information"]
        widgets = {
            "date_of_birth": DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        num_contact = cleaned_data.get("contact_information")

        if len(num_contact) != 11:
            raise forms.ValidationError("Enter Valid Contact No.")

        name = cleaned_data.get("name")
        contact_information = cleaned_data.get("contact_information")
        date_of_birth = cleaned_data.get("date_of_birth")
        gender = cleaned_data.get("gender")

        filter_condition = (
            Q(name=name)
            & Q(contact_information=contact_information)
            & Q(date_of_birth=date_of_birth)
            & Q(gender=gender)
        )

        record_exists = Patient.objects.filter(filter_condition).exists()

        if record_exists:
            raise forms.ValidationError("Patient Name and Contact No. Exists")

        return super().clean()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "date_of_birth", "gender", "contact_information"]
        widgets = {
            "date_of_birth": DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        num_contact = cleaned_data.get("contact_information")

        if len(num_contact) != 11:
            raise forms.ValidationError("Enter Valid Contact No.")

        name = cleaned_data.get("name")
        contact_information = cleaned_data.get("contact_information")

        filter_condition = Q(name=name) & Q(contact_information=contact_information)

        record_exists = Patient.objects.filter(filter_condition).exists()

        if record_exists:
            raise forms.ValidationError("Patient Name and Contact No. Exists")

        return super().clean()


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = [
            "allergies",
            "medications",
            "previous_illnesses",
            "surgeries",
            "diagnosis_note",
        ]


class AppointmentForm(forms.ModelForm):
    Name = forms.CharField(max_length=50)
    class Meta:
        model = Appointment
        fields = ["appointment_date", "appointment_time", "additional_notes", "appointment_doctor"]

        Dr_Choices = [("Dr Ash", "Dr Ash"), ("Dr Bob", "Dr Bob"), ("Cath", "Cath"),]
        Time_Choices = [(f"{hour:02}:{minute:02}", f"{hour:02}:{minute:02}:00") for hour in range(8, 20) for minute in range(0, 60, 10)]

        widgets = {
            "appointment_date": DateInput(attrs={"type": "date"}),
            "appointment_time": Select(choices= Time_Choices ),
            "appointment_doctor": Select(choices= Dr_Choices ),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")
        appointment_doctor = cleaned_data.get("appointment_doctor")

        given_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M:%S")

        if given_datetime < datetime.now():
            raise forms.ValidationError("Invalid Appointment")


        filter_condition = (
            Q(appointment_date=appointment_date)
            & Q(appointment_time=appointment_time)
            & Q(appointment_doctor=appointment_doctor)
        )

        record_exists = Appointment.objects.filter(filter_condition).exists()

        if record_exists:
            raise forms.ValidationError("Appointment Not Available")

        return super().clean()
