# Generated by Django 4.2.1 on 2023-12-14 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0027_container_purchase_currency_exchange_settlement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container_purchase',
            old_name='vendor',
            new_name='vens',
        ),
    ]