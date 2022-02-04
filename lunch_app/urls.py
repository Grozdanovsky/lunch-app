from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('lunches', views.LunchViewSet)
router.register('ingredients',views.IngredientsViewSet)

urlpatterns = [
    path('random/',views.RandomLunch.as_view())  
]

urlpatterns += router.urls



   



