# forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image', help_text='SVG, PNG, JPG, or GIF (MAX. 800x400px)')
