# Generated by Django 4.2.4 on 2023-10-24 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomberos', '0014_alter_prestamo_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='Mantencion',
            field=models.DateField(),
        ),
    ]
