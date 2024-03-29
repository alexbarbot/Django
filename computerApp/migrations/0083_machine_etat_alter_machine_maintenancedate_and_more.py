# Generated by Django 4.1.7 on 2023-06-06 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0082_personnel_mail_alter_machine_maintenancedate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="machine",
            name="etat",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 6, 9, 1, 5, 937744)
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 6, 9, 1, 5, 975251)
            ),
        ),
    ]
