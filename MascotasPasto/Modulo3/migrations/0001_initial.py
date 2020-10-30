# Generated by Django 3.1.1 on 2020-10-30 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('abreviatura', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='razas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('abreviatura', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('id_tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Modulo3.tipos')),
            ],
        ),
        migrations.CreateModel(
            name='mascotas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('tiene_vacunas', models.BooleanField()),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('id_raza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Modulo3.razas')),
                ('id_tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Modulo3.tipos')),
            ],
        ),
    ]