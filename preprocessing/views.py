from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .function import data_preprocessing, data_vis, get_image
from django.contrib.auth.decorators import login_required
from .models import FileUpload
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT
from django.core.files.base import ContentFile


def index(request):
    FileUpload.objects.all().delete()

    return render(request, 'index.html')


def preprocessing(request):

    FileUpload.objects.all().delete()

    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)
        

        if uploadfile.is_valid():
            
            uploadfile.save()
            uploaded_file = request.FILES['upload_file']
            wl_corr = uploadfile.cleaned_data['wl_corr']
            wl_range_start = uploadfile.cleaned_data['wl_range_start']
            wl_range_end = uploadfile.cleaned_data['wl_range_end']


            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            data = pd.read_csv(file_path, index_col=0).T
            y = data_preprocessing(data, file_path, wl_corr)

            obj = FileUpload.objects.latest("upload_file")

            obj.upload_file.name = 'preprocessed_data.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)
            y.T.to_csv(new_file_path)

     
            data_vis(new_file_path, wl_range_start, wl_range_end)
            graph = get_image()
            
            uploadfile = FileUpload.objects.all()

            return render(request, 'results.html', {'uploadfile': uploadfile, 'graph': graph})


    else:
        uploadfile = UploadFileForm()
        return render(request, 'preprocessing.html', {'uploadfile': uploadfile})


def results(request):
    uploadfile = FileUpload.objects.all()
    return render(request, 'results.html', {'uploadfile': uploadfile})

