# Generated by Django 4.2.1 on 2023-09-15 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0008_alter_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='maintenance_history',
        ),
    ]
