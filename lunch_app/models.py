from re import T
from statistics import mode
from django.db import models


class Ingredients(models.Model):
    title = models.CharField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.title
    

class Lunch(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)


class Review(models.Model):
    lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE,related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


    
