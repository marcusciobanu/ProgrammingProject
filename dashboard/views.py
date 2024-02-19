from django.shortcuts import render
from .forms import CreateExerciseForm


def home(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        username = request.user.username
        return render(request, 'home/home.html', {'name': name, 'username': username})
    else:
        return render(request, 'error/not-logged.html')


def create(request):
    if request.method == 'POST':
        form = CreateExerciseForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
        else:
            form = CreateExerciseForm()
    else:
        form = CreateExerciseForm()
    return render(request, 'exercisebank/create.html', {'form': form})
