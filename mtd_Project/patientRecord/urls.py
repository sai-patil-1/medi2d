from django.urls import path
from . import views

urlpatterns = [

    # Patient, Add New Patient, Edit Patient
    path("", views.patient_a, name="patient_a"),
    path("new_patient/", views.new_patient, name="new_patient"),
    path("edit_patient/", views.edit_patient, name="edit_patient"),

    # Appointment
    path("add_appointment/", views.add_appointment_a, name="add_appointment_a"),
    path("appointment/", views.appointment_a, name="appointment_a"),

    # History
    path("history/", views.history_a, name="history_a"),
    path("history/add_history", views.history_b, name="history_b"),

    # Get details of selected row
    path("ajax_output_row/", views.ajax_row_edit_patient),
    path("new_patient/ajax_output_row/", views.ajax_row_edit_patient, name = "ajax_row_edit_patient"),
    path("edit_patient/ajax_output_row/", views.ajax_row_edit_patient, name = "ajax_row_edit_patient"),
    path("add_appointment/ajax_output_row/", views.ajax_row_edit_patient, name = "ajax_row_edit_patient"),

]
