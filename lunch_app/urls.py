from django.urls import path
from . import views


urlpatterns = [
    path('lunches/',views.lunch_list),
    path('lunches/<int:pk>/',views.lunch_detail),
    path('random',views.random_lunch),
    path('ingredients/',views.ingredients_list),
    path('ingredients/<int:pk>',views.ingredients_detail),
]
