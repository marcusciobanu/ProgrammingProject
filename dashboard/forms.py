from django import forms
from .models import Workout, WorkoutExercise, Set, ExerciseBank
from django.forms import modelformset_factory


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = []


class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise']

    def __init__(self, *args, **kwargs):
        super(WorkoutExerciseForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].queryset = ExerciseBank.objects.all()


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['reps', 'weight', 'set_type']
        widgets = {
            'reps': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': '0.01'}),
            'set_type': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'reps': 'Repetitions',
            'weight': 'Weight (lbs or kg)',
            'set_type': 'Type of Set',
        }
        help_texts = {
            'reps': 'Enter the number of reps completed.',
            'weight': 'Enter the weight used for this set.',
            'set_type': 'Select the type of set performed.',
        }

    def clean(self):
        cleaned_data = super().clean()
        reps = cleaned_data.get('reps')
        weight = cleaned_data.get('weight')

        if reps and reps <= 0:
            self.add_error('reps', 'Number of repetitions must be positive.')

        if weight and weight < 0:
            self.add_error('weight', 'Weight must be a positive number.')

        return cleaned_data


SetFormset = modelformset_factory(
    Set,
    form=SetForm,
    extra=1,  # Number of empty forms to display
    can_delete=True  # Allows the option to delete forms if needed
)
