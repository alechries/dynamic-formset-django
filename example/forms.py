from django import forms
from . import models


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['name']
        widgets = {
             'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name',
                'id': 'NameInput',
             }),
        }


class AdditionForm(forms.ModelForm):
    class Meta:
        model = models.Addition
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