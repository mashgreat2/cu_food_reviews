# Generated by Django 2.1.1 on 2018-09-08 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operating_hours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('start_timestamp', models.BigIntegerField(null=True)),
                ('end_timestamp', models.BigIntegerField(null=True)),
                ('start_time', models.CharField(max_length=50, null=True)),
                ('end_time', models.CharField(max_length=50, null=True)),
                ('operating_hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operating_hours.OperatingHour')),
            ],
        ),
    ]
