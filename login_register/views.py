from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("You are at the login page.")
