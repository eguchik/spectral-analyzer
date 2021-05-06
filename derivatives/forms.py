from django import forms
from django.contrib.admin import widgets
import os
from .models import FileUpload2


class UploadFileForm2(forms.ModelForm):

    class Meta:
        # 利用するモデルクラスを指定
        model = FileUpload2

        # 利用するモデルのフィールドを指定
        fields = ('upload_file', 
        'n_differential', 
        'polyorder', 
        'window_length', 
        'n_smooth',)
        # ウィジェットを上書き
        widgets = {
            'polyorder': forms.RadioSelect,
        }