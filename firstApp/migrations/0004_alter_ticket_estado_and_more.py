# Generated by Django 5.1.2 on 2024-11-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_alter_ticket_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='estado',
            field=models.CharField(choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado'), ('en_proceso', 'En Proceso')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='satisfaccion_cliente',
            field=models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], max_length=50),
        ),
    ]
