# Generated by Django 2.1.1 on 2018-09-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.BigIntegerField(null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('eatery_name', models.CharField(max_length=200, null=True)),
                ('about', models.TextField(null=True)),
                ('about_short', models.TextField(null=True)),
                ('cornell_dining', models.BooleanField(default=True)),
                ('op_hours_calc', models.CharField(max_length=100, null=True)),
                ('op_hours_calc_desc', models.TextField(null=True)),
                ('google_calendar_id', models.CharField(max_length=200, null=True)),
                ('online_ordering', models.BooleanField(default=False)),
                ('online_order_url', models.URLField(null=True)),
                ('contact_phone', models.CharField(max_length=30, null=True)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('service_unit_id', models.BigIntegerField(null=True)),
                ('campus_area', models.CharField(max_length=100, null=True)),
                ('campus_area_short', models.CharField(max_length=50, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('location_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]