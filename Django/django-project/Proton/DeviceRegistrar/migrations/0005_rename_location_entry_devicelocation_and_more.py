# Generated by Django 4.0.6 on 2022-08-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceRegistrar', '0004_alter_entry_mac_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='Location',
            new_name='DeviceLocation',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='MAC_Id',
            new_name='Id',
        ),
    ]
