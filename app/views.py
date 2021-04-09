from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .function import write_into_csv, data_preprocessing, data_vis
from django.contrib.auth.decorators import login_required
from .models import FileUpload
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT



@login_required
def index(request):

    FileUpload.objects.all().delete() # モデルの初期化

    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)
        

        if uploadfile.is_valid():
            
            uploadfile.save() # modelへ保存される


            uploaded_file = request.FILES['upload_file']
            wl_corr = uploadfile.cleaned_data['wl_corr']

            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            data = pd.read_csv(file_path, index_col=0).T
            data_preprocessing(data, file_path, wl_corr)
            data_vis(MEDIA_ROOT)

            
        return render(request, 'index2.html', {'uploadfile': uploadfile})

    else:
        uploadfile = UploadFileForm()
        return render(request, 'index.html', {'uploadfile': uploadfile})

def index2(request):
    file_obj = FileUpload.objects.all()
    return render(request, 'index2.html', {'file_obj': file_obj})