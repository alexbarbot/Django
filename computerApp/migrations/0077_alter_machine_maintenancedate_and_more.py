# Generated by Django 4.1.7 on 2023-06-04 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0076_alter_machine_maintenancedate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 4, 20, 13, 46, 126246)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 4, 20, 13, 46, 146740)
            ),
        ),
    ]
