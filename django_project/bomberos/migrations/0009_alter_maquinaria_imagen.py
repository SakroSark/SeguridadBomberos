# Generated by Django 4.2.4 on 2023-10-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomberos', '0008_maquinaria_mantencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='Imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
