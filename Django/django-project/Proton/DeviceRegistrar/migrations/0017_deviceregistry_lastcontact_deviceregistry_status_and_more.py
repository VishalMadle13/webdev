
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceRegistrar', '0016_remove_deviceregistry_status_devicelastupdate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceregistry',
            name='LastContact',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='deviceregistry',
            name='Status',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.DeleteModel(
            name='DeviceLastUpdate',
        ),
    ]
