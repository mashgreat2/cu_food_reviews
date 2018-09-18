# Generated by Django 2.1.1 on 2018-09-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealitem',
            old_name='meal_event',
            new_name='meal_category',
        ),
        migrations.AddField(
            model_name='mealitem',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
