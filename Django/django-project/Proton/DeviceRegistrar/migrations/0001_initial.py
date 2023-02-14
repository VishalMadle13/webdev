# Generated by Django 4.0.6 on 2022-08-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('MAC_Id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('DeviceType', models.CharField(max_length=12)),
                ('DeviceVersion', models.PositiveIntegerField()),
                ('Location', models.CharField(max_length=12)),
                ('PrimaryGroup', models.CharField(max_length=50)),
                ('SecondaryGroup', models.CharField(max_length=50)),
                ('LastContact', models.TimeField()),
                ('Status', models.CharField(max_length=4)),
            ],
        ),
    ]