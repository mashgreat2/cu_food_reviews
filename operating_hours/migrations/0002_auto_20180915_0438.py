# Generated by Django 2.1.1 on 2018-09-15 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operating_hours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatinghour',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]