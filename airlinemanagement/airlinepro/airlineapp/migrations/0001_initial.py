# Generated by Django 5.1.1 on 2024-09-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=10, unique=True)),
                ('dep_airport', models.CharField(max_length=100)),
                ('dep_date', models.DateField()),
                ('dep_time', models.TimeField()),
                ('arr_airport', models.CharField(max_length=100)),
                ('arr_date', models.DateField()),
                ('arr_time', models.TimeField()),
            ],
        ),
    ]
