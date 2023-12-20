# Generated by Django 4.2.1 on 2023-10-09 15:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0016_expense_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('con', models.DecimalField(decimal_places=2, max_digits=10, unique=True)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freight_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pol', models.CharField(max_length=50)),
                ('Pofd', models.CharField(max_length=50)),
                ('Pot1', models.CharField(max_length=50)),
                ('Pot2', models.CharField(max_length=50)),
                ('Shipper', models.CharField(max_length=500)),
                ('Booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Sailing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(default=1, max_length=20)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('Carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.carrier')),
                ('Commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.commodity')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.agent')),
                ('cntr_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.contract_owner')),
                ('freight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.freight_category')),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.vessel')),
            ],
        ),
    ]
