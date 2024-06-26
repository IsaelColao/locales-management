# Generated by Django 5.0.6 on 2024-06-24 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0004_alter_local_edificio_pertenece"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
                ("correo", models.CharField(max_length=100)),
                ("contrasena", models.CharField(max_length=100)),
                ("nivel", models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name="arearesponsabilidad", old_name="nombre_area", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="arearesponsabilidad",
            old_name="responsable_area",
            new_name="responsable",
        ),
        migrations.RenameField(
            model_name="centrocosto", old_name="nombre_centro", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="centrocosto",
            old_name="responsable_centro",
            new_name="responsable",
        ),
        migrations.RenameField(
            model_name="edificio", old_name="codigo_edificio", new_name="codigo",
        ),
        migrations.RenameField(
            model_name="edificio", old_name="nombre_edificio", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="local", old_name="codigo_local", new_name="codigo",
        ),
        migrations.RenameField(
            model_name="local", old_name="funcion_local", new_name="funcion",
        ),
        migrations.RenameField(
            model_name="local", old_name="nombre_local", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="local", old_name="tipo_local", new_name="tipo",
        ),
        migrations.RenameField(
            model_name="reservacion", old_name="nombre_reserva", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="sede", old_name="codigo_sede", new_name="codigo",
        ),
        migrations.RenameField(
            model_name="sede", old_name="direccion_sede", new_name="director",
        ),
        migrations.RenameField(
            model_name="sede", old_name="director_sede", new_name="nombre",
        ),
        migrations.RemoveField(model_name="sede", name="nombre_sede",),
        migrations.RemoveField(model_name="sede", name="telefono_sede",),
        migrations.AddField(
            model_name="sede",
            name="direccion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="sede",
            name="telefono",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="local",
            name="local_pertenece",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sublocal",
                to="backend.local",
            ),
        ),
        migrations.AlterField(
            model_name="local",
            name="sede_pertenece",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sede_local",
                to="backend.sede",
            ),
        ),
    ]
