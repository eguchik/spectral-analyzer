from django.shortcuts import render
from .forms import UploadFileForm
from .plot_graph import plot_data
from .models import FileUpload
import pandas as pd
import os
from myproject.settings import MEDIA_ROOT
from .derivspc import DerivSpc



def derivatives(request):
    
    FileUpload.objects.all().delete() # データベースの初期化
    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)
        

        if uploadfile.is_valid():
            
            uploadfile.save() 

            uploaded_file = request.FILES['upload_file']
            n_differential = uploadfile.cleaned_data['n_differential']
            polyorder = uploadfile.cleaned_data['polyorder']
            window_length = uploadfile.cleaned_data['window_length']
            n_smooth = uploadfile.cleaned_data['n_smooth']

            

            file_path = os.path.join(MEDIA_ROOT, uploaded_file.name)
            data = pd.read_csv(file_path, index_col=0)

            derivspc = DerivSpc(n_differential=n_differential,
                        polyorder=polyorder,
                        window_length=window_length,
                        n_smooth=n_smooth)
                        
            y = derivspc.fit(data)

            obj = FileUpload.objects.latest("upload_file")
            obj.upload_file.name = obj.upload_file.name[:-4] + '_derivatives.csv'
            obj.save()
            new_file_path = os.path.join(MEDIA_ROOT, obj.upload_file.name)


            y.to_csv(new_file_path)
            plot = plot_data(new_file_path, 0)
            plot2 = plot_data(new_file_path, 1)

            return render(request, 'results.html', {'obj': obj, 'plot': plot, 'plot2': plot2})


    else:
        uploadfile = UploadFileForm()
        return render(request, 'derivatives.html', {'uploadfile': uploadfile})