# Generated by Django 2.1.1 on 2018-12-11 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_reviews', '0002_review_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=4, null=True),
        ),
    ]
