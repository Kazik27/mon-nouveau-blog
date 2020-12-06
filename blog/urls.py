from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
]

#Pour afficher les équipements:

#urlpatterns = [
   # path('', views.equipement_list, name='equipement_list'),
#]
