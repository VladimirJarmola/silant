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


def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='system/errors/error_page.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница не была найдена, или перемещена', 
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='system/errors/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request=request, template_name='system/errors/error_page.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'У Вас нет доступа к этой странице, обратитесь к администратору!',
    })
