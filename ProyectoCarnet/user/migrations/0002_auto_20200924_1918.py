# Generated by Django 3.1 on 2020-09-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
