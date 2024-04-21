from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CreateExerciseForm
from .models import Exercise, Workout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        username = request.user.username
        return render(request, "home/home.html", {"name": name, "username": username})
    else:
        return render(request, "error/not-logged.html")


def create(request):
    if request.user.is_authenticated:
        user_exercises = Exercise.objects.filter(user=request.user)
        if request.method == "POST":
            form = CreateExerciseForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                form = CreateExerciseForm()
            else:
                form = CreateExerciseForm()
        else:
            form = CreateExerciseForm()
        return render(
            request,
            "exercisebank/create.html",
            {"form": form, "user_exercises": user_exercises},
        )
    else:
        return render(request, "error/not-logged.html")


# Imported Django function decorator which ensures the user is logged in
@login_required
def delete_exercise(request, exercise_id):
    if request.method == "POST":
        exercise = Exercise.objects.get(id=exercise_id, user=request.user)
        exercise.delete()
        return HttpResponseRedirect(reverse("create"))
    else:
        return HttpResponseRedirect(reverse("create"))


@login_required
def start_workout(request):
    new_workout = Workout(user=request.user, start_time=timezone.now())
    new_workout.save()

    return redirect("add_exercise", workout_id=new_workout.id)
