# Generated by Django 4.2.1 on 2023-12-12 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0024_booking_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Shipper',
            new_name='ship',
        ),
    ]
