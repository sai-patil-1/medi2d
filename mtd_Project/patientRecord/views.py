# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient
from django.contrib import messages
from .forms import PatientForm, MedicalHistoryForm, AppointmentForm, PatientForm_Edit
from datetime import date
from .models import Patient, MedicalHistory, Appointment
from datetime import datetime
from django.http import JsonResponse

# Variable to save selected patient row
global_selected_patient_id = [1]


# View Functions redirecting to URLs
@login_required
@permission_required(["account.view_patient_info"], login_url = "/patient/")
def patient_a(request):
    """
    Redirect to 'Patient' web page.

    """
    # retrieve data from model to load in table
    all_members = Patient.objects.all()
    print("all_members", all_members)

    return render(
        request,
        "patientRecord/patient_info.html",
        {
            "all_members": all_members,
        },
    )


@login_required
@permission_required(["account.add_edit_patient_info"], login_url = "/patient/")
def new_patient(request):
    """
    On Button click 'Add New Patient'

    """
    # retrieve data from model to load in table
    all_members = Patient.objects.all()

    # defining form for input data
    form_class = PatientForm(request.POST)

    if request.method == "POST":
        if form_class.is_valid():
            current_user = request.user
            uname = str(current_user)

            new_user = form_class.save(commit=False)
            new_user.entry_name = str(current_user)
            new_user.save()

            messages.success(request, "Profile Added successfully")
            return render(
                request, "patientRecord/patient_info.html", {"all_members": all_members}
            )
        else:
            messages.error(request, "Error Occurred.")

    else:
        form_class = PatientForm()

    return render(
        request,
        "patientRecord/new_patient.html",
        {
            "form_class": form_class,
            "all_members": all_members,
        },
    )


@login_required
@permission_required(["account.add_edit_patient_info"], login_url = "/patient/")
def edit_patient(request):
    """
    On button click 'Edit Patient Data'

    """
    all_members = Patient.objects.all()

    patient_id = global_selected_patient_id[0]

    rev_obj = Patient.objects.get(pk=patient_id)
    initial_dict = {
        "name": rev_obj.name,
        "date_of_birth": rev_obj.date_of_birth,
        "gender": rev_obj.gender,
        "contact_information": rev_obj.contact_information,
    }
    print(initial_dict)

    form_class = PatientForm_Edit(request.POST)
    if request.method == "POST":
        if form_class.is_valid():
            current_user = request.user
            uname = str(current_user)

            e = Patient.objects.get(pk=patient_id)

            e.name = form_class.cleaned_data["name"]
            e.date_of_birth = form_class.cleaned_data["date_of_birth"]
            e.gender = form_class.cleaned_data["gender"]
            e.contact_information = form_class.cleaned_data["contact_information"]
            e.entry_date = date.today()
            e.entry_name = uname
            e.save()

            messages.success(request, "Profile Updated successfully")
            return render(
                request, "patientRecord/patient_info.html", {"all_members": all_members}
            )
        else:
            messages.error(request, "Error Occurred.")

    else:
        form_class = PatientForm_Edit(initial=initial_dict)

    return render(
        request,
        "patientRecord/edit_patient.html",
        {
            "form_class": form_class,
            "all_members": all_members,
        },
    )


@login_required
@permission_required(
    ["account.view_patient_info", "account.view_edit_appointment"], login_url = "/patient/"
)
def add_appointment_a(request):
    all_members = Patient.objects.all()

    patient_id = global_selected_patient_id[0]
    rev_obj = Patient.objects.get(pk=patient_id)
    initial_dict = {
        "Name": rev_obj.name,
        "appointment_date": date.today(),
    }

    form_class = AppointmentForm(request.POST)
    if request.method == "POST":
        if form_class.is_valid():
            new_user = form_class.save(commit=False)
            new_user.patient = Patient.objects.get(pk=patient_id)
            new_user.save()

            messages.success(request, "Profile Updated successfully")

        else:
            messages.error(request, "Error Occurred.")

    else:
        form_class = AppointmentForm(initial=initial_dict)



    return render(
        request,
        "patientRecord/book_appointment.html",
        {
            "form_class": form_class,
            "all_members": all_members,
        },
    )



@login_required
@permission_required(
    ["account.view_patient_info", "account.view_edit_appointment"], login_url = "/patient/"
)
def appointment_a(request):
    """
    Function to redirect to 'Appointment' web page.

    """
    all_members = Appointment.objects.filter(appointment_date=date.today())


    if request.method == "POST":
        print("In Post", date.today())
        print(request.POST['date'])

        print(request.POST['appt'])
        all_members = Appointment.objects.filter(appointment_date=request.POST['date'], appointment_doctor=request.POST['appt'])

        return render(
            request,
            "patientRecord/appointment_info.html",
            {
                "all_members": all_members,
                'date': request.POST['date'],
                'appt': request.POST['appt'],
            },
        )


    else:
        return render(
            request,
            "patientRecord/appointment_info.html",
            {
                "all_members": all_members,
                'date': date.today().strftime('%Y-%m-%d'),
                'appt': 'Dr Ash',
            },
        )


@login_required
@permission_required(["account.view_patient_med_history"], login_url = "/patient/")
def history_a(request):
    # all_members = Patient.objects.all()

    patient_id = global_selected_patient_id[0]

    if request.method == "POST":
        member_history = MedicalHistory.objects.filter(patient__pk=patient_id)

        return render(
            request,
            "patientRecord/m_history_2.html",
            {
                "all_members": member_history,
                "patient_id": patient_id,
            },
        )

    else:
        member_history = MedicalHistory.objects.all()

        return render(
            request,
            "patientRecord/m_history_1.html",
            {
                "all_members": member_history,
            },
        )


@login_required
@permission_required(["account.edit_patient_med_history"], login_url = "/patient/")
def history_b(request):
    """
    On Button click 'Add New Record' on 'Medical History' page.

    """
    patient_id = global_selected_patient_id[0]
    member_history = MedicalHistory.objects.filter(patient__pk=patient_id)

    member_instance = Patient.objects.get(pk=patient_id)
    print("member_instance-", member_instance)

    # defining form for input data
    form_class = MedicalHistoryForm(request.POST)

    if request.method == "POST":
        if form_class.is_valid():
            current_user = request.user

            new_user = form_class.save(commit=False)
            new_user.patient = Patient.objects.get(pk=patient_id)
            new_user.diagnosed_by = str(current_user)

            new_user.save()

            messages.success(request, "Profile Added successfully")
            return render(
                request,
                "patientRecord/m_history_2.html",
                {"all_members": member_history},
            )

        else:
            messages.error(request, "Error Occurred.")

    else:
        form_class = MedicalHistoryForm()

    return render(
        request,
        "patientRecord/m_history_3.html",
        {
            "all_members": member_history,
            "form_class": form_class,
        },
    )


def ajax_row_edit_patient(request):
    """
    AJAX call from 'patient_info.html'
    To get Patient ID of selected row from Datatable
    """
    row_selected = request.POST["text"]

    row_selected = row_selected.split('","')

    row_selected = [
        row_selected[0].replace('["', ""),
        row_selected[1],
        row_selected[2],
        row_selected[3].replace('"]', ""),
    ]

    # print(row_selected)

    try:
        patient_record = Patient.objects.get(
            name=row_selected[0],
            gender=row_selected[2],
            contact_information=row_selected[3],
        )

        global_selected_patient_id[0] = patient_record.patient_id
        print("Patient Id - ", patient_record.patient_id)

    except Exception as e:
        print("Error In 'ajax_row_view' -", e)

    return HttpResponse(request.POST["text"])
