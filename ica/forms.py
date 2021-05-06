from django import forms
from django.contrib.admin import widgets
import os
from .models import FileUpload


class UploadFileForm(forms.ModelForm):

    class Meta:
        # 利用するモデルクラスを指定
        model = FileUpload

        # 利用するモデルのフィールドを指定
        fields = ('upload_file', 'algo', 'n_components')