from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from .models import Lunch,Ingredients
from .serializers import LunchSerializer,IngredientsSerializer
import random
import json
from pprint import pprint

class LunchViewSet(ModelViewSet):
    
    queryset = Lunch.objects.prefetch_related('ingredients').all()
    serializer_class = LunchSerializer

class RandomLunch(APIView):
    
    def get(self,request):
        queryset = Lunch.objects.prefetch_related('ingredients').all()
        lunch = random.choice(queryset)
        serializer = LunchSerializer(lunch)
        return Response(serializer.data) 

class IngredientsViewSet(ModelViewSet):
    
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer