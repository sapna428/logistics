# Generated by Django 4.2.1 on 2023-12-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0038_remove_exchange_tran_id_exchange_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency_exchange',
            old_name='type',
            new_name='to',
        ),
        migrations.AddField(
            model_name='currency_exchange',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currency_exchange',
            name='fom',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='currency_exchange',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Exchange',
        ),
    ]