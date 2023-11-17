# Generated by Django 4.2.4 on 2023-10-24 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bomberos', '0012_remove_prestamo_idmaquinaria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSalud',
            fields=[
                ('idAreaSalud', models.AutoField(primary_key=True, serialize=False)),
                ('NombreArea', models.CharField(max_length=255)),
                ('Telefono', models.CharField(max_length=255)),
                ('CorreoElectronico', models.CharField(max_length=255)),
                ('ResponsableAreaSalud', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('idPrestamo', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=255)),
                ('Descripcion', models.CharField(max_length=255)),
                ('ElementoPrestado', models.CharField(max_length=255)),
                ('FechaPrestamo', models.DateField()),
                ('Estado', models.CharField(max_length=255)),
                ('IdMaquinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.maquinaria')),
                ('idAreaSalud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomberos.areasalud')),
            ],
        ),
    ]
