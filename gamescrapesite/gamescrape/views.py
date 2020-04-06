from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def zelda(request):
    return render(request, 'zelda.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def contactus(request):
    return render(request, 'contactus.html', {})
