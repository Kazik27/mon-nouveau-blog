from django.shortcuts import render
from django.utils import timezone
from .models import Animal
from .models import Equipement



def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'blog/animal_list.html', {'animals': animals})

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'blog/animal_list.html', {'equipements': equipements})