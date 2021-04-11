from django import forms
from django.contrib.admin import widgets
import os
from .models import FileUpload, FileUpload2


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('upload_file', 'wl_corr',)

class UploadFileForm2(forms.ModelForm):

    class Meta:
        model = FileUpload2
        fields = ('upload_file', 
        'n_differential', 
        'polyorder', 
        'window_length', 
        'n_smooth',)