# Generated by Django 2.1.1 on 2018-09-18 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_eatery_name_short'),
        ('operating_hours', '0005_auto_20180918_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatinghour',
            name='location',
        ),
        migrations.AddField(
            model_name='operatinghour',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]
