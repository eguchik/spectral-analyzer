from django import forms
from django.contrib.admin import widgets
import os
from .models import FileUpload


class UploadFileForm(forms.ModelForm):

    class Meta:
        # 利用するモデルクラスを指定
        model = FileUpload

        # 利用するモデルのフィールドを指定
        fields = ('upload_file', 
        'n_differential', 
        'polyorder', 
        'window_length', 
        'n_smooth')
        # ウィジェットを上書き
        widgets = {
            'polyorder': forms.RadioSelect,
        }