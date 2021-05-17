from django import forms
from django.contrib.admin import widgets
import os
from .models import FileUpload


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('upload_file', 'wl_corr',)