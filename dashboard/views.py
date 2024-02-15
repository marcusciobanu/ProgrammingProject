from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Workout


def dashboard(request):
    return render(request, 'dashboard/base.html')


# WORK IN PROGRESS
@login_required
def create_workout(request):
    if request.method == 'POST':
        workout = Workout(user=request.user)
        workout.save()
        return redirect('some_view_name')
    return render(request, 'your_template_name.html')
# WORK IN PROGRESS
