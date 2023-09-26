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
Clone the repository.
Then in the command prompt type:
(after entering the project..)
```
pip install -r requirements.txt
```
to install required packages and dependencies.  
Now, go to 'mtd_Project' directory by typing command
```
cd mtd_Project
```
Then to run the project, type the command:
```
py manage.py runserver
```
then copy the local url and run it on your browser...

Note-
- Create make migration file by 'python manage.py makemigrations'
- Create Super User by 'python manage.py createsuperuser', give required acceses to registered users and add few dummy entries in database manually.

- To Edit Patient Data or to Add Medical History, first Select Patient.
- Setup SMTP to send Mail.
