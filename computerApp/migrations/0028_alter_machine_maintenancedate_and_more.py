# Generated by Django 4.1.7 on 2023-05-14 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0027_alter_machine_maintenancedate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 14, 19, 20, 4, 472623)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 14, 19, 20, 4, 492622)
            ),
        ),
    ]