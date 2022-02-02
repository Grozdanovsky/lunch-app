import imp
from itertools import product
import re
from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lunch,Ingredients
from .serializers import LunchSerializer,IngredientsSerializer
import random

@api_view(["GET",'POST'])
def lunch_list(request):
    if request.method == "GET":
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        serialzier = LunchSerializer(queryset, many=True)
        return Response(serialzier.data)
    elif request.method == "POST":
        serialzier = LunchSerializer(data=request.data)
        serialzier.is_valid(raise_exception=True)
        serialzier.save()
        return Response(serialzier.data, status=status.HTTP_201_CREATED)


@api_view(["GET","PUT","DELETE"])
def lunch_detail(request,pk):
    lunch = get_object_or_404(Lunch.objects.prefetch_related('ingredients'), pk=pk)
    if request.method == "GET":
        serializer = LunchSerializer(lunch)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = LunchSerializer(lunch,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        lunch.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


@api_view()
def random_lunch(request):
    queryset = Lunch.objects.prefetch_related('ingredients').all()
    lunch = random.choice(queryset)
    serializer = LunchSerializer(lunch)
    return Response(serializer.data)

@api_view(["GET","POST"])
def ingredients_list(request):
    if request.method == "GET":
        queryset = Ingredients.objects.all()
        serialzier = IngredientsSerializer(queryset,many=True)
        return Response(serialzier.data)
    elif request.method == "POST":
        serializer = IngredientsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def ingredients_detail(request,pk):
    ingredient = get_object_or_404(Ingredients,pk=pk)
    if request.method == "GET":
        serializer = IngredientsSerializer(ingredient)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = IngredientsSerializer(ingredient, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

