from django import forms
from . import models


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'count']
        widgets = {
             'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name',
                'id': 'NameInput',
             }),
             'count': forms.NumberInput(attrs={
                'id': 'CountInput',
                'class': 'form-control',
             }),
        }


class AdditionAForm(forms.ModelForm):
    class Meta:
        model = models.AdditionA
        count_type = forms.ModelChoiceField(
            queryset=models.TypeA.objects.all(),
            empty_label=None,
            to_field_name="count_type",
        )
        fields = ['id', 'name', 'count', 'count_type']
        widgets = {
            'id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'id': 'NameInput',
                'class': 'form-control',
                'placeholder': 'Введите ключевые слова',
            }),
            'count': forms.NumberInput(attrs={
                'id': 'CountInput',
                'class': 'form-control',
            }),
            'count_type': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class AdditionBForm(forms.ModelForm):
    class Meta:
        model = models.AdditionB
        fields = ['id', 'description', 'image']
        widgets = {
            'id': forms.HiddenInput(),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter addition description',
                'rows': '1',
                'id': 'DescriptionInput',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'id': 'ImageInput',
            }),
        }