from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('lunches', views.LunchViewSet)
router.register('ingredients',views.IngredientsViewSet)

products_router = routers.NestedDefaultRouter(router,'lunches',lookup='lunch')
products_router.register('reviews',views.ReviewViewSet,basename='lunch-reviews')
urlpatterns = [
    path('random/',views.RandomLunch.as_view()),
     
]

urlpatterns += router.urls
urlpatterns += products_router.urls



   



