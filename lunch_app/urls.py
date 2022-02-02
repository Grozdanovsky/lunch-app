from django.urls import path
from . import views


urlpatterns = [
    path('lunches/',views.LunchList.as_view()),
    path('lunches/<int:pk>/',views.LunchDetail.as_view()),
    path('random',views.RandomLunch.as_view()),
    path('ingredients/',views.IngredientsList.as_view()),
    path('ingredients/<int:pk>',views.IngredientsDetail.as_view()),
]
