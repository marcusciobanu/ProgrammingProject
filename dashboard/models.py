from django.db import models
from django.conf import settings


class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_taken = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, related_name='workouts')

    def __str__(self):
        return f"Workout by {self.user.username}"


class Set(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    SET_TYPES = [
        ('failure', 'Failure'),
        ('dropset', 'Dropset'),
        ('warmup', 'Warmup'),
    ]
    set_type = models.CharField(max_length=7, choices=SET_TYPES)

    def __str__(self):
        return f"{self.exercise.name} - {self.set_type} set"
