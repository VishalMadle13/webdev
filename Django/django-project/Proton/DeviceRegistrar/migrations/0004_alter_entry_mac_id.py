# Generated by Django 4.0.6 on 2022-08-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceRegistrar', '0003_remove_entry_deviceversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='MAC_Id',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]
