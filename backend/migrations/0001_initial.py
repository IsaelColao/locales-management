# Generated by Django 5.0 on 2024-04-19 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_Costo',
            fields=[
                ('id_centro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_centro', models.CharField(max_length=100)),
                ('responsable_centro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id_edificio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_edificio', models.CharField(max_length=100)),
                ('codigo_edificio', models.CharField(max_length=100)),
                ('niveles', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sede', models.CharField(max_length=100)),
                ('codigo_sede', models.CharField(max_length=100)),
                ('director_sede', models.CharField(max_length=100)),
                ('direccion_sede', models.CharField(max_length=100)),
                ('telefono_sede', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Area_Responsabilidad',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=100)),
                ('responsable_area', models.CharField(max_length=100)),
                ('centro_pertenece', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.centro_costo')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.AutoField(primary_key=True, serialize=False)),
                ('nivel_local', models.IntegerField(max_length=8)),
                ('nombre_local', models.CharField(max_length=100)),
                ('codigo_local', models.CharField(max_length=100)),
                ('funcion_local', models.CharField(max_length=100)),
                ('tipo_local', models.CharField(max_length=100)),
                ('estado_constructivo', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('reservable', models.BooleanField()),
                ('area_responsab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.area_responsabilidad')),
                ('edificio_pertenece', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.edificio')),
                ('sede_pertenece', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.sede')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id_reservacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_reserva', models.CharField(max_length=100)),
                ('cargo_reserv', models.CharField(max_length=100)),
                ('tiempo_reserv', models.CharField(max_length=100)),
                ('uso_reserv', models.CharField(max_length=100)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.local')),
            ],
        ),
        migrations.AddField(
            model_name='edificio',
            name='sede_pertenece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.sede'),
        ),
    ]