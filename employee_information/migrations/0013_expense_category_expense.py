# Generated by Django 4.2.1 on 2023-09-28 13:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0012_roleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=1, max_length=20)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('expense_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.expense_category')),
                ('veh_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.vehicle_category')),
            ],
        ),
    ]
