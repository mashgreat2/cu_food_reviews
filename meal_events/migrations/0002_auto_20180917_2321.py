# Generated by Django 2.1.1 on 2018-09-17 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealevent',
            name='operating_hour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operating_hours.OperatingHour'),
        ),
    ]
