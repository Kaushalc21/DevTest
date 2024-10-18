from django import forms
from .models import UploadedFile  # Ensure UploadedFile is properly defined in models.py

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']  # This should correspond to the file field in the model
        labels = {
            'file': 'Select a file to upload',
        }
