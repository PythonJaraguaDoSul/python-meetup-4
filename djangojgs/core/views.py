from djangojgs.core.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        return userauth(request)

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def userauth(request):
    form = LoginForm(request.POST)

    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'login.html', {'form': form})

    login(request, user)
    return HttpResponseRedirect(r('home'), {'user': user})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(r('user_login'))

def cerveja_portifolio(request):
    if request.method == "GET":
        return render(request, "portifolio.html")

