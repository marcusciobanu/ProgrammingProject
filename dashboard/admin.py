from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise, Set


class SetInline(admin.TabularInline):
    model = Set
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'time_taken')
    search_fields = ['user__username']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout', 'exercise')
    search_fields = ['workout__user__username']
    inlines = [SetInline]


class SetAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_exercise', 'reps', 'weight', 'set_type')
    search_fields = ['workout_exercise__exercise__name', 'set_type']


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
admin.site.register(Set, SetAdmin)
