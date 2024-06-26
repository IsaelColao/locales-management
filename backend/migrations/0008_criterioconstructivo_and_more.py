# Generated by Django 5.0.6 on 2024-06-25 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_alter_local_ancho_alter_local_largo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CriterioConstructivo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                (
                    "nombre_corto",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
        ),
        migrations.RemoveField(model_name="local", name="estado_constructivo",),
        migrations.RemoveField(model_name="local", name="observaciones",),
        migrations.AddField(
            model_name="local",
            name="nombre_corto",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name="Evaluacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("observaciones", models.TextField(blank=True, null=True)),
                (
                    "criterio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="backend.criterioconstructivo",
                    ),
                ),
                (
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="backend.local"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="local",
            name="criterios_constructivos",
            field=models.ManyToManyField(
                through="backend.Evaluacion", to="backend.criterioconstructivo"
            ),
        ),
    ]
