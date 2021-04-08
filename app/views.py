from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .function import write_into_csv, data_preprocessing
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    if request.method == 'POST':
        uploadfile = UploadFileForm(request.POST, request.FILES)

        if uploadfile.is_valid():

            uploaded_file = request.FILES['file']
            wl_corr = uploadfile.cleaned_data['wl_corr']
            preprocessed_data = data_preprocessing(uploaded_file, wl_corr)
            response = write_into_csv(preprocessed_data)

            return response
    

    else:
        uploadfile = UploadFileForm()
        
        return render(request, 'index.html', {'form': uploadfile})