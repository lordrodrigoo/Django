from django.urls import path

from . import views

app_name = 'recipes'


urlpatterns = [
    path('', views.home, name='home' ), # HOME
    path('recipes/<int:id>/', views.recipe, name='recipe' ),

 
]