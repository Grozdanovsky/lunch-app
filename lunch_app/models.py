from statistics import mode
from django.db import models


class Ingredients(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    

class Lunch(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)

    
