from django.shortcuts import render


def manage_sets(request, workout_exercise_id):
    WorkoutExerciseInstance = get_object_or_404(WorkoutExercise, pk=workout_exercise_id)
    if request.method == 'POST':
        formset = SetFormset(request.POST, queryset=Set.objects.filter(workout_exercise=WorkoutExerciseInstance))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.workout_exercise = WorkoutExerciseInstance
                instance.save()
            formset.save_m2m()  # Save many-to-many data for the formset
            # Redirect or indicate success
    else:
        formset = SetFormset(queryset=Set.objects.filter(workout_exercise=WorkoutExerciseInstance))

    return render(request, 'manage_sets.html', {'formset': formset})


def dashboard(request):
    return render(request, 'dashboard/base.html')
