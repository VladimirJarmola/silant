# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Мой Силант',
        'content': 'Информация о комплектации и технических характеристиках Вашей техники'
    }
    return render(request, 'cars/index.html', context)
