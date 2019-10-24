from django import forms
from .models import Theme
from ckeditor.widgets import CKEditorWidget


class HintForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'hintCount', 'hint1', 'hint2', 'hint3', 'hint4', 'hint5', 'hint6', 'hint7', 'hint8', 'hint9',
                  'hint10', 'hint11', 'hint12', 'hint13', 'hint14', 'hint15', 'hint16', 'hint17', 'hint18', 'hint19',
                  'hint20', 'sub_hint1', 'sub_hint2', 'sub_hint3', 'sub_hint4', 'sub_hint5', 'sub_hint6', 'sub_hint7',
                  'sub_hint8', 'sub_hint9', 'sub_hint10', 'sub_hint11', 'sub_hint12', 'sub_hint13', 'sub_hint14',
                  'sub_hint15', 'sub_hint16', 'sub_hint17', 'sub_hint18', 'sub_hint19', 'sub_hint20', 'hint21', 'hint22',
                  'hint23', 'hint24', 'hint25', 'hint26', 'hint27', 'hint28', 'hint29', 'hint30', 'sub_hint21', 'sub_hint22',
                  'sub_hint23', 'sub_hint24', 'sub_hint25', 'sub_hint26', 'sub_hint27', 'sub_hint28', 'sub_hint29', 'sub_hint30',
                  'enterKey', 'textHint1', 'textHint2', 'textHint3', 'textHint4', 'textHint5', 'textHint6', 'textHint7', 'textHint8',
                  'textHint9', 'textHint10', 'textHint11', 'textHint12', 'textHint13', 'textHint14', 'textHint15', 'textHint16',
                  'textHint17', 'textHint18', 'textHint19', 'textHint20', 'textHint21', 'textHint21', 'textHint22', 'textHint23',
                  'textHint24', 'textHint25', 'textHint26', 'textHint27', 'textHint28', 'textHint29', 'textHint30',
                  'sub_textHint1', 'sub_textHint2', 'sub_textHint3', 'sub_textHint4', 'sub_textHint5', 'sub_textHint6', 'sub_textHint7',
                  'sub_textHint8', 'sub_textHint9', 'sub_textHint10', 'sub_textHint11', 'sub_textHint12', 'sub_textHint13', 'sub_textHint14',
                  'sub_textHint15', 'sub_textHint16', 'sub_textHint17', 'sub_textHint18', 'sub_textHint19', 'sub_textHint20', 'sub_textHint21',
                  'sub_textHint22', 'sub_textHint23', 'sub_textHint24', 'sub_textHint25', 'sub_textHint26', 'sub_textHint27',
                  'sub_textHint28', 'sub_textHint29', 'sub_textHint30']
        widgets = {
            'textHint1': CKEditorWidget(
                attrs={
                    'style': 'width: 100%'
                }
            ),
            'textHint2': CKEditorWidget(),
            'textHint3': CKEditorWidget(),
            'textHint4': CKEditorWidget(),
            'textHint5': CKEditorWidget(),
            'textHint6': CKEditorWidget,
            'textHint7': CKEditorWidget,
            'textHint8': CKEditorWidget,
            'textHint9': CKEditorWidget,
            'textHint10': CKEditorWidget,
            'textHint11': CKEditorWidget,
            'textHint12': CKEditorWidget,
            'textHint13': CKEditorWidget,
            'textHint14': CKEditorWidget,
            'textHint15': CKEditorWidget,
            'textHint16': CKEditorWidget,
            'textHint17': CKEditorWidget,
            'textHint18': CKEditorWidget,
            'textHint19': CKEditorWidget,
            'textHint20': CKEditorWidget,
            'textHint21': CKEditorWidget,
            'textHint22': CKEditorWidget,
            'textHint23': CKEditorWidget,
            'textHint24': CKEditorWidget,
            'textHint25': CKEditorWidget,
            'textHint26': CKEditorWidget,
            'textHint27': CKEditorWidget,
            'textHint28': CKEditorWidget,
            'textHint29': CKEditorWidget,
            'textHint30': CKEditorWidget,

            'sub_textHint1': CKEditorWidget(),
            'sub_textHint2': CKEditorWidget(),
            'sub_textHint3': CKEditorWidget(),
            'sub_textHint4': CKEditorWidget(),
            'sub_textHint5': CKEditorWidget(),
            'sub_textHint6': CKEditorWidget(),
            'sub_textHint7': CKEditorWidget(),
            'sub_textHint8': CKEditorWidget(),
            'sub_textHint9': CKEditorWidget(),
            'sub_textHint10': CKEditorWidget(),
            'sub_textHint11': CKEditorWidget(),
            'sub_textHint12': CKEditorWidget(),
            'sub_textHint13': CKEditorWidget(),
            'sub_textHint14': CKEditorWidget(),
            'sub_textHint15': CKEditorWidget(),
            'sub_textHint16': CKEditorWidget(),
            'sub_textHint17': CKEditorWidget(),
            'sub_textHint18': CKEditorWidget(),
            'sub_textHint19': CKEditorWidget(),
            'sub_textHint20': CKEditorWidget(),
            'sub_textHint21': CKEditorWidget(),
            'sub_textHint22': CKEditorWidget(),
            'sub_textHint23': CKEditorWidget(),
            'sub_textHint24': CKEditorWidget(),
            'sub_textHint25': CKEditorWidget(),
            'sub_textHint26': CKEditorWidget(),
            'sub_textHint27': CKEditorWidget(),
            'sub_textHint28': CKEditorWidget(),
            'sub_textHint29': CKEditorWidget(),
            'sub_textHint30': CKEditorWidget(),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'border-color:black',
                }
            ),
            'enterKey': forms.TextInput(
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
            'hint21': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint21': forms.FileInput(
                attrs={
                    'id': 'sub21_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint22': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint22': forms.FileInput(
                attrs={
                    'id': 'sub22_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint23': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint23': forms.FileInput(
                attrs={
                    'id': 'sub23_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint24': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint24': forms.FileInput(
                attrs={
                    'id': 'sub24_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint25': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint25': forms.FileInput(
                attrs={
                    'id': 'sub25_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint26': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint26': forms.FileInput(
                attrs={
                    'id': 'sub26_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint27': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint27': forms.FileInput(
                attrs={
                    'id': 'sub27_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint28': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint28': forms.FileInput(
                attrs={
                    'id': 'sub28_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint29': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint29': forms.FileInput(
                attrs={
                    'id': 'sub29_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint30': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint30': forms.FileInput(
                attrs={
                    'id': 'sub30_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
        }
