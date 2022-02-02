from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Lunch,Ingredients
from .serializers import LunchSerializer,IngredientsSerializer
import random


class LunchList(ListCreateAPIView):
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        serializer_class = LunchSerializer

    
class LunchDetail(RetrieveUpdateDestroyAPIView):
    queryset = Lunch.objects.prefetch_related('ingredients')
    serializer_class = LunchSerializer

class RandomLunch(APIView):
    def get(self,request):
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        lunch = random.choice(queryset)
        serializer = LunchSerializer(lunch)
        return Response(serializer.data)


class IngredientsList(ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    


class IngredientsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


