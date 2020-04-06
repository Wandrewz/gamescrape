from django.shortcuts import render
from .models import Game

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games':games})

def zelda(request):
    obj = Game.objects.get(id=1)
    return render(request, 'zelda.html', {'obj':obj})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def contactus(request):
    return render(request, 'contactus.html', {})
