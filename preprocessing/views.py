from django.shortcuts import render
from .forms import UploadFileForm
from .models import FileUpload
import os
from myproject.settings import MEDIA_ROOT
from .spectral_preprocessing import preprocessing
from .plot_graph import plot_data
import pandas as pd


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

            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            
            data = pd.read_csv(file_path, index_col=0)
            data = data.sub(data.iloc[:, 0], axis='index')
            data = data.sub(data.loc[wl_corr, :], axis="columns")
            data.drop(columns=data.columns[0], inplace=True)

            obj = FileUpload.objects.latest("upload_file")
            obj.upload_file.name = 'preprocessed_data.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)
            data.to_csv(new_file_path)
            plot= plot_data(new_file_path)      
            uploadfile = FileUpload.objects.all()

            return render(request, 'results.html', {'uploadfile': uploadfile, 'plot': plot})


    else:
        uploadfile = UploadFileForm()
        return render(request, 'preprocessing.html', {'uploadfile': uploadfile})


def results(request):
    uploadfile = FileUpload.objects.all()
    return render(request, 'results.html', {'uploadfile': uploadfile})

