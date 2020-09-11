# Generated by Django 3.0.7 on 2020-09-10 20:00

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_carnet', models.IntegerField()),
                ('foto', models.ImageField(upload_to='')),
                ('otorgamiento', models.DateField()),
                ('vencimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoSanguineo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacionalidad', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=70)),
                ('donante', models.BooleanField()),
                ('nacimiento', models.DateField()),
                ('grupo_s', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.GrupoSanguineo')),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.Nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCarnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('n_carnet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.Carnet')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.Persona')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Seguro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('num_poliza', models.IntegerField(max_length=30)),
                ('tel', models.IntegerField(max_length=15)),
                ('tel_emergencia', models.IntegerField(max_length=15)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.TipoSeguro')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=45)),
                ('año', models.DateField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Cedula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cedula', models.CharField(max_length=45)),
                ('patente', models.CharField(max_length=15)),
                ('nombre_registro', models.CharField(max_length=45)),
                ('num_motor', models.IntegerField()),
                ('num_chasis', models.IntegerField()),
                ('emision', models.DateField()),
                ('vencimiento', models.DateField()),
                ('seguro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.Seguro')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.TipoVehiculo')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.Modelo')),
            ],
        ),
        migrations.AddField(
            model_name='carnet',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCarnet.Persona'),
        ),
        migrations.AddField(
            model_name='carnet',
            name='tipo_carnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppCarnet.TipoCarnet'),
        ),
    ]