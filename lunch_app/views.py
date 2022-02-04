from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from .models import Lunch,Ingredients, Review
from .serializers import LunchSerializer,IngredientsSerializer, ReviewSerializer
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


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(lunch_id = self.kwargs['lunch_pk'])


    def get_serializer_context(self):
        return {"lunch_id":self.kwargs['lunch_pk']}