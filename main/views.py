from django.shortcuts import render
from .models import Bascet

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def tovars(request):
    products = Bascet.objects.all()
    return render(request, 'main/tovars.html', {"products":products})
