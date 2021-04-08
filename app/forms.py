from django import forms
from django.contrib.admin import widgets
import os


class UploadFileForm(forms.Form):
    file = forms.FileField()
    wl_corr = forms.IntegerField()



class DerSpcForm(forms.Form):
    file = forms.FileField()
    n_differential = forms.IntegerField()
    window_length = forms.IntegerField()
    polyorder = forms.IntegerField()
    n_smooth = forms.IntegerField()

