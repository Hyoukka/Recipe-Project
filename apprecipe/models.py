from django.db import models
from datetime import datetime

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    preparation_time = models.IntegerField()
    recipe_yield = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    recipe_date = models.DateTimeField(default=datetime.now, blank=True)