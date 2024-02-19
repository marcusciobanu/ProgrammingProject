from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        username = request.user.username
        return render(request, 'home/home.html', {'name': name, 'username': username})
    else:
        return render(request, 'error/not-logged.html')

