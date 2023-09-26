# medi2d
Medical Records Management System.

## Objectives
* To build a simple medical records management system using Django.
* The system should allow healthcare professionals to create and manage patient records, including basic patient information, medical history, and appointment scheduling.

### Subtasks-
* Registeration for Healthcare Professional's account with name, email, and password.
* User Login and Logout.
* User authentication and authorization.
* User group creation and permission management.
* Database model for patient records, including fields such as name, date of birth, gender, contact information, and medical history.
* Patient record Management by User (Create, view, edit, and delete).
* Search and Sort functionality that allows healthcare professionals for patient records based on patient name, date of birth, or appointment date.
* Unit tests.

## Setting up the project
1) Clone the repository.

2) To install required packages and dependencies.
```
pip install -r requirements.txt
```

3) Create make migration file
```
python manage.py migrate
```

4) Create SuperUser
```
python manage.py createsuperuser
```

5) Go to 'mtd_Project' directory. Then to run the project, type the command:
```
py manage.py runserver
```
6) Give required acceses to registered users and add few dummy entries in database manually. (http://127.0.0.1:8000/admin/)

7) Go to 'http://127.0.0.1:8000/account/'

Note-
- Application fetches data from database, so first create dummy entries to avoid errors.
- To Edit Patient Data or to Add Medical History, first Select Patient.
- Setup SMTP to send Mail.
