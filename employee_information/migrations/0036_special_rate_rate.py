# Generated by Django 4.2.1 on 2023-12-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0035_remove_container_slot_pur_id_container_slot_con_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_rate',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
