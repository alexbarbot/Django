# Generated by Django 4.1.7 on 2023-05-12 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0025_alter_machine_maintenancedate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 12, 12, 51, 3, 935459)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 12, 12, 51, 3, 956022)
            ),
        ),
    ]
