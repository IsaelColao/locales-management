# Generated by Django 5.0.6 on 2024-06-25 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0012_evaluacion_nota"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="arearesponsabilidad",
            options={"verbose_name_plural": "Áreas de Responsabilidad"},
        ),
        migrations.AlterModelOptions(
            name="centrocosto", options={"verbose_name_plural": "Centros de Costo"},
        ),
        migrations.AlterModelOptions(
            name="criterioconstructivo",
            options={"verbose_name_plural": "Criterios Conswvszxstructivos"},
        ),
        migrations.AlterModelOptions(
            name="edificio", options={"verbose_name_plural": "Edificios"},
        ),
        migrations.AlterModelOptions(
            name="local", options={"verbose_name_plural": "Locales"},
        ),
        migrations.AlterModelOptions(
            name="reservacion", options={"verbose_name_plural": "Reservaciones"},
        ),
        migrations.AlterModelOptions(
            name="responsable", options={"verbose_name_plural": "Responsables"},
        ),
        migrations.AlterModelOptions(
            name="sede", options={"verbose_name_plural": "Sedes"},
        ),
    ]
