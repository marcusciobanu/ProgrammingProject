from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def homepage(request):
    return render(request, "index/index.html")


def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # Separates logic of form submission from user who wants to access plain login page
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("../dashboard/home")
    else:
        # Renders blank form for users who are sending GET requests
        form = AuthenticationForm()
    # Sends form data to be rendered, either blank or with user's inputs in so they remain there if the webstie is refreshed
    return render(request, "login/login.html", {"form": form})


def registerpage(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("../dashboard/home")
        # Creates a user and then immediately logs them in for convenience
    else:
        form = CustomUserCreationForm()
    return render(request, "register/register.html", {"form": form})
