from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Lunch,Ingredients
from .serializers import LunchSerializer,IngredientsSerializer
import random
import json
from pprint import pprint

class LunchList(APIView):
    def get(self,request):
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        serialzier = LunchSerializer(queryset, many=True)
        return Response(serialzier.data)
    
    
    def post(self,request):
        
        serialzier = LunchSerializer(data=request.data)
        serialzier.is_valid(raise_exception=True)
        serialzier.save()
        return Response(serialzier.data, status=status.HTTP_201_CREATED)

class LunchDetail(APIView):
    def get(self,request,pk):
        lunch = get_object_or_404(Lunch.objects.prefetch_related('ingredients'), pk=pk) 
        serializer = LunchSerializer(lunch)
        return Response(serializer.data)
    
    def put(self,request,pk):
        lunch = get_object_or_404(Lunch.objects.prefetch_related('ingredients'), pk=pk)
        serializer = LunchSerializer(lunch,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        lunch = get_object_or_404(Lunch.objects.prefetch_related('ingredients'), pk=pk)
        lunch.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class RandomLunch(APIView):
    def get(self,request):
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        lunch = random.choice(queryset)
        serializer = LunchSerializer(lunch)
        return Response(serializer.data) 

class IngredientsList(APIView):
    def get(self,request):
        queryset = Ingredients.objects.all()
        serialzier = IngredientsSerializer(queryset,many=True)
        return Response(serialzier.data)
    def post(self,request):
        serializer = IngredientsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

class IngredientsDetail(APIView):
    def get(self,request,pk):
        ingredient = get_object_or_404(Ingredients,pk=pk)
        serializer = IngredientsSerializer(ingredient)
        
        return Response(serializer.data)

    def put(self,request,pk):
        ingredient = get_object_or_404(Ingredients,pk=pk)
        serializer = IngredientsSerializer(ingredient, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        ingredient = get_object_or_404(Ingredients,pk=pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

