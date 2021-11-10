from django.shortcuts import render
from .models import Bascet

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'main/index.html', {'title':'Главная страница','num_visits':num_visits})

def about(request):
    data = {'title':'О нас'}
    return render(request, 'main/about.html', data)

def contacts(request):
    data = {'title':'Контакты'}
    return render(request, 'main/contacts.html',data)


def tovars(request):
    products = Bascet.objects.all()
    data = {'title':'Товары', 'products':products}
    return render(request, 'main/tovars.html',data)
