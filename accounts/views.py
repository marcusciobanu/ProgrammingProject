from django.shortcuts import render
from .forms import CustomUserCreationForm


def homepage(request):
    return render(request, 'index/index.html')


def loginpage(request):
    return render(request, 'login/login.html')


def registerpage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})
