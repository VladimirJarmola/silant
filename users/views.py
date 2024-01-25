from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


from users.forms import UserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы успешно вошли в свой аккаунт!")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('cars:cars'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта!")
    auth.logout(request)
    return redirect(reverse('main:index'))
