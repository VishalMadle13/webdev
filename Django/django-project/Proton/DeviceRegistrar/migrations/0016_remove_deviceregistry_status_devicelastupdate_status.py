# Generated by Django 4.0.6 on 2022-08-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceRegistrar', '0015_remove_deviceregistry_lastcontact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceregistry',
            name='Status',
        ),
        migrations.AddField(
            model_name='devicelastupdate',
            name='Status',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
