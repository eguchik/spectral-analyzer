from django.shortcuts import render
from .forms import UploadFileForm
from .ica import icar
from .models import FileUpload
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT
from .plot_graph import plot_data



def ica(request):
    # データベースの初期化
    FileUpload.objects.all().delete()

    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)
        

        if uploadfile.is_valid():        
            uploadfile.save()
            uploaded_file = request.FILES['upload_file']
            algo = uploadfile.cleaned_data['algo']
            n_components = uploadfile.cleaned_data['n_components']
            wl_range_start = uploadfile.cleaned_data['wl_range_start']
            wl_range_end = uploadfile.cleaned_data['wl_range_end']
            



            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            
            ics = icar(file_path, algo, n_components, wl_range_start, wl_range_end)

        
            obj = FileUpload.objects.latest("upload_file")

            obj.upload_file.name = obj.upload_file.name[:-4] + '_ica.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)
            ics.to_csv(new_file_path, index=False)

            plot = plot_data(new_file_path)

            return render(request, 'results.html', {'obj': obj, 'plot': plot})


    else:
        uploadfile = UploadFileForm()
        return render(request, 'ica.html', {'uploadfile': uploadfile})


def results(request):
    uploadfile = FileUpload.objects.all()
    return render(request, 'results.html', {'obj': obj})


