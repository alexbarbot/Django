# Generated by Django 4.1.7 on 2023-05-22 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "computerApp",
            "0037_alter_machine_maintenancedate_alter_machine_nom_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 22, 9, 35, 41, 295766)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 22, 9, 35, 41, 315588)
            ),
        ),
    ]