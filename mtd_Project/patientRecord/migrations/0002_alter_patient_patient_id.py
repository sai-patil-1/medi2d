# Generated by Django 4.2.5 on 2023-09-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
