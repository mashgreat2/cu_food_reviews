from django.db import models

# Create your models here.
from meal_events.models import MealEvent


class MealCategory(models.Model):
    name = models.CharField(null=True, max_length=100)
    sort_index = models.IntegerField(null=True)
    meal_event = models.ForeignKey(MealEvent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name