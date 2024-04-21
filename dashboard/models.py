from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_started = models.DateTimeField(auto_now_add=True)
    time_taken = models.IntegerField(help_text="Duration of the workout in minutes")


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class Set(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE)
    weight = models.FloatField(help_text="Weight used for the set")
    SET_TYPES = [
        ("warmup", "Warmup"),
        ("dropset", "Dropset"),
        ("failure", "Failure"),
    ]
    set_type = models.CharField(
        max_length=7, choices=SET_TYPES, help_text="Type of the set"
    )
    reps = models.IntegerField(help_text="Number of repetitions")
