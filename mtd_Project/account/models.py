from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Meta:
        permissions = (
            ("view_patient_info", "Can view patient info"),
            ("add_edit_patient_info", "Can edit patient info"),
            ("view_edit_appointment", "Can edit patient appointment"),
            ("view_patient_med_history", "Can view patient medical history"),
            ("edit_patient_med_history", "Can edit patient medical history"),
        )
