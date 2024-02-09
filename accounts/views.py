from django.shortcuts import render


def homepage(request):
    return render(request, 'index/index.html')


def login(request):
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'register/register.html')
