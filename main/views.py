# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):

    context = {
        'title': 'Мой Силант',
        'content': 'Информация о комплектации и технических характеристиках Вашей техники',
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('cars:cars'))
    else:
        return render(request, 'main/index.html', context)
