# Generated by Django 5.1.4 on 2025-01-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_alter_servicio_imagen_alter_servicio_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
