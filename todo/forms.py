from django import forms

from .models import ToDo

from django.utils import timezone

class NewToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }