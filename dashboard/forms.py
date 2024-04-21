from django.forms import ModelForm
from .models import Exercise


class CreateExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ["name"]

    # Overrides inherited method to extract user from the keyword arguments. Once complete, hands back the rest of the arguments to the supermethod for regular processing
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(CreateExerciseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        exercise = super(CreateExerciseForm, self).save(commit=False)
        exercise.user = self.user
        if commit:
            exercise.save()
        return exercise
