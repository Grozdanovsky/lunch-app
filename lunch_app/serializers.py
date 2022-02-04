from asyncore import read
from re import T
from rest_framework import serializers
from .models import Lunch,Ingredients, Review


class IngredientsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredients
        fields = ['id','title']
        


class LunchSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many = True)
    class Meta:
        model = Lunch
        fields = ['id','title','description','recipe','ingredients']
        depth = 1
        

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        lunch = Lunch.objects.create(**validated_data)
        for ingredient in ingredients_data:
            ingredient,created = Ingredients.objects.get_or_create(title = ingredient['title'])
            lunch.ingredients.add(ingredient)
        return lunch

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']
    
    def create(self, validated_data):
        lunch_id = self.context['lunch_id']
        return Review.objects.create(lunch_id=lunch_id, **validated_data)


    