from django.db import models

# Create your models here.
from meal_categories.models import MealCategory


class MealItem(models.Model):
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(null=True, max_length=200)
    is_healthy = models.BooleanField(default=False)
    sort_index = models.IntegerField(null=True)
    meal_category = models.ManyToManyField(MealCategory)