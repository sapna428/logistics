# Generated by Django 4.2.1 on 2023-09-15 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0010_vehicle_date_added_vehicle_date_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_type',
            new_name='vehicle_id',
        ),
    ]