# Generated by Django 3.1 on 2020-09-17 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usuario_validado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='validado',
        ),
    ]