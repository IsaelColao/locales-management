# Generated by Django 5.0.6 on 2024-06-24 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_alter_edificio_sede_pertenece_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="local",
            name="edificio_pertenece",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="locales",
                to="backend.edificio",
            ),
        ),
    ]
