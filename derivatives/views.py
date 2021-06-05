from django.shortcuts import render
from .forms import UploadFileForm2
from .models import FileUpload2
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT
from .diffspc import DiffSpc
from .plot_graph import plot_data



def derivatives(request):

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
            plot= plot_data(new_file_path)      
        
            
            uploadfile = FileUpload2.objects.all()

            return render(request, 'results.html', {'uploadfile': uploadfile, 'plot': plot})


    else:
        uploadfile = UploadFileForm2()
        return render(request, 'derivatives.html', {'uploadfile': uploadfile})


def results(request):
    uploadfile = FileUpload2.objects.all()
    return render(request, 'results.html', {'uploadfile': uploadfile})

