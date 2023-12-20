# forms.py

from django import forms
from .models import FormData

class UploadForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
