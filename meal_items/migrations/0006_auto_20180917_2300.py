# Generated by Django 2.1.1 on 2018-09-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_items', '0005_auto_20180917_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealitem',
            name='meal_category',
            field=models.ManyToManyField(to='meal_categories.MealCategory'),
        ),
    ]
