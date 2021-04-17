from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadFileForm, UploadFileForm2
from .function import data_preprocessing, data_vis, get_image, data_vis2
from django.contrib.auth.decorators import login_required
from .models import FileUpload, FileUpload2
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT
from django.core.files.base import ContentFile
from .diffspc import DiffSpc


def index(request):
    FileUpload.objects.all().delete()
    FileUpload2.objects.all().delete()

    return render(request, 'index.html')


def analysis1(request):

    FileUpload.objects.all().delete() # データベースの初期化

    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)
        

        if uploadfile.is_valid():
            
            uploadfile.save()
            uploaded_file = request.FILES['upload_file']
            wl_corr = uploadfile.cleaned_data['wl_corr']


            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            data = pd.read_csv(file_path, index_col=0).T
            y = data_preprocessing(data, file_path, wl_corr)

            obj = FileUpload.objects.latest("upload_file")

            obj.upload_file.name = 'preprocessed_data.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)
            y.T.to_csv(new_file_path)

     
            data_vis(new_file_path)
            graph = get_image()
            
            uploadfile = FileUpload.objects.all()

            return render(request, 'output1.html', {'uploadfile': uploadfile, 'graph': graph})


    else:
        uploadfile = UploadFileForm()
        return render(request, 'analysis1.html', {'uploadfile': uploadfile})


def output1(request):
    uploadfile = FileUpload.objects.all()
    return render(request, 'output1.html', {'uploadfile': uploadfile})


def analysis2(request):

    FileUpload2.objects.all().delete() # データベースの初期化

    if request.method == 'POST':
        uploadfile = UploadFileForm2(request.POST, request.FILES)
        

        if uploadfile.is_valid():
            
            uploadfile.save() 

            uploaded_file = request.FILES['upload_file']
            n_differential = uploadfile.cleaned_data['n_differential']
            polyorder = uploadfile.cleaned_data['polyorder']
            window_length = uploadfile.cleaned_data['window_length']
            n_smooth = uploadfile.cleaned_data['n_smooth']

            

            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            data = pd.read_csv(file_path, index_col=0).T

            diffspc = DiffSpc(n_differential=n_differential, polyorder=polyorder, window_length=window_length, n_smooth=n_smooth)
            y = diffspc.fit(data)

            obj = FileUpload2.objects.latest("upload_file")
            obj.upload_file.name = 'differentiated_data.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)


            y.T.to_csv(new_file_path)
        
            data_vis2(new_file_path)
            graph = get_image()
            
            uploadfile = FileUpload2.objects.all()

            return render(request, 'output2.html', {'uploadfile': uploadfile, 'graph': graph})


    else:
        uploadfile = UploadFileForm2()
        return render(request, 'analysis2.html', {'uploadfile': uploadfile})


def output2(request):
    uploadfile = FileUpload2.objects.all()
    return render(request, 'output2.html', {'uploadfile': uploadfile})

