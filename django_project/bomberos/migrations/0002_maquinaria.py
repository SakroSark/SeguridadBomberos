# Generated by Django 4.2.4 on 2023-10-23 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bomberos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maquinaria',
            fields=[
                ('IdMaquinaria', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=255)),
                ('CantidadProducto', models.IntegerField()),
                ('FechaIngreso', models.DateField()),
                ('Estado', models.CharField(max_length=255)),
                ('Imagen', models.CharField(max_length=255)),
                ('Tipo', models.CharField(max_length=255)),
                ('Gabetas', models.CharField(max_length=255)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]