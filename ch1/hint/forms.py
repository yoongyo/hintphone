from django import forms
from .models import Theme


class HintForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'hintCount', 'hint1', 'hint2', 'hint3', 'hint4', 'hint5', 'hint6', 'hint7', 'hint8', 'hint9',
                  'hint10', 'hint11', 'hint12', 'hint13', 'hint14', 'hint15', 'hint16', 'hint17', 'hint18', 'hint19',
                  'hint20', 'sub_hint1', 'sub_hint2', 'sub_hint3', 'sub_hint4', 'sub_hint5', 'sub_hint6', 'sub_hint7',
                  'sub_hint8', 'sub_hint9', 'sub_hint10', 'sub_hint11', 'sub_hint12', 'sub_hint13', 'sub_hint14',
                  'sub_hint15', 'sub_hint16', 'sub_hint17', 'sub_hint18', 'sub_hint19', 'sub_hint20']
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
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint1': forms.FileInput(
                attrs={
                    'id': 'sub1_file',
                    'style': 'border-color:black;display: none',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint2': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint2': forms.FileInput(
                attrs={
                    'id': 'sub2_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint3': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint3': forms.FileInput(
                attrs={
                    'id': 'sub3_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint4': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint4': forms.FileInput(
                attrs={
                    'id': 'sub4_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint5': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint5': forms.FileInput(
                attrs={
                    'id': 'sub5_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint6': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint6': forms.FileInput(
                attrs={
                    'id': 'sub6_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint7': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint7': forms.FileInput(
                attrs={
                    'id': 'sub7_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint8': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint8': forms.FileInput(
                attrs={
                    'id': 'sub8_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint9': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint9': forms.FileInput(
                attrs={
                    'id': 'sub9_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint10': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint10': forms.FileInput(
                attrs={
                    'id': 'sub10_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint11': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint11': forms.FileInput(
                attrs={
                    'id': 'sub11_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint12': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint12': forms.FileInput(
                attrs={
                    'id': 'sub12_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint13': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint13': forms.FileInput(
                attrs={
                    'id': 'sub13_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint14': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint14': forms.FileInput(
                attrs={
                    'id': 'sub14_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint15': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint15': forms.FileInput(
                attrs={
                    'id': 'sub15_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint16': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint16': forms.FileInput(
                attrs={
                    'id': 'sub16_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint17': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint17': forms.FileInput(
                attrs={
                    'id': 'sub17_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint18': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint18': forms.FileInput(
                attrs={
                    'id': 'sub18_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint19': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint19': forms.FileInput(
                attrs={
                    'id': 'sub19_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint20': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint20': forms.FileInput(
                attrs={
                    'id': 'sub20_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
        }
