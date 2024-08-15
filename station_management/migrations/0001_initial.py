# Generated by Django 4.2.15 on 2024-08-15 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('capacity', models.FloatField()),
                ('current_charge', models.FloatField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SwappingStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('battery_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IoTData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('voltage', models.FloatField()),
                ('current', models.FloatField()),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_management.battery')),
            ],
        ),
        migrations.AddField(
            model_name='battery',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='station_management.swappingstation'),
        ),
    ]
