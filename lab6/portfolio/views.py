from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/home.html')


import datetime


# Create your views here.
def index_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def about_view(request):
    return render(request, 'portfolio/home.html')


def quizzview(request):
    return render(request, 'portfolio/quizz.html')

def projetosview(request):
    return render(request, 'portfolio/projetos.html')