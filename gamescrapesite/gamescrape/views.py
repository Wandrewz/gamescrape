from django.shortcuts import render
from .models import Game

def index(request):
    games = Game.objects.all().order_by('title')
    return render(request, 'index.html', {'games':games})

def details(request, slug):
    obj = Game.objects.get(slug=slug)
    return render(request, 'details.html', {'obj':obj})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def contactus(request):
    return render(request, 'contactus.html', {})
