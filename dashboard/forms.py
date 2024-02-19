from django.forms import ModelForm
from .models import Exercise


class CreateExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateExerciseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        exercise = super(CreateExerciseForm, self).save(commit=False)
        exercise.user = self.user
        if commit:
            exercise.save()
        return exercise
