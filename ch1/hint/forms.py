from django import forms
from .models import Theme


class HintForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'hintCount', 'hint1', 'hint2', 'hint3', 'hint4', 'hint5', 'hint6', 'hint7', 'hint8', 'hint9',
                  'hint10', 'hint11', 'hint12', 'hint13', 'hint14', 'hint15', 'hint16', 'hint17', 'hint18', 'hint19',
                  'hint20']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hintCount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint1': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint2': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint3': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint4': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint5': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint6': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint7': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint8': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint9': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint10': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint11': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint12': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint13': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint14': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint15': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint16': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint17': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint18': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint19': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'hint20': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
        }
