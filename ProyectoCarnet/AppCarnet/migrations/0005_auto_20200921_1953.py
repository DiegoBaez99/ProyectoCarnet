# Generated by Django 3.1.1 on 2020-09-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarnet', '0004_remove_cedula_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='foto',
            field=models.ImageField(null=True, upload_to='albums/images/'),
        ),
    ]