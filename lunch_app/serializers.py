from rest_framework import serializers
from .models import Lunch,Ingredients


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id','title']


class LunchSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True, read_only= True)
    class Meta:
        model = Lunch
        fields = ['id','title','description','recipe','ingredients']


      

    