# Generated by Django 4.1.7 on 2023-06-06 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "computerApp",
            "0084_alter_machine_maintenancedate_alter_personnel_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 6, 9, 33, 52, 894956)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 6, 9, 33, 52, 916485)
            ),
        ),
    ]
