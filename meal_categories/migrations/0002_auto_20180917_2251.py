# Generated by Django 2.1.1 on 2018-09-17 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealcategory',
            name='meal_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meal_events.MealEvent'),
        ),
    ]
