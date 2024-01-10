# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'home',
        'content': 'content'
    }
    return render(request, 'cars/index.html', context)
