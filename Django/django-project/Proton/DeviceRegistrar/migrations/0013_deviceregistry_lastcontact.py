# Generated by Django 4.0.6 on 2022-08-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceRegistrar', '0012_deviceregistry_delete_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceregistry',
            name='LastContact',
            field=models.TimeField(null=True),
        ),
    ]
