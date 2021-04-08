import csv
from django.http import HttpResponse
import pandas as pd


def write_into_csv(csv_data):

    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="download.csv"'

    return response


def data_preprocessing(csv_file, wl_corr=None):

    X = pd.read_csv(csv_file, index_col=0).T

    if wl_corr == None:
        wl_corr = X.columns[-1]

    y = X.copy()
    y -= y.iloc[0, :]
    y.drop(y.index[0], inplace=True)
    y = y.sub(y[wl_corr], axis='index')

    return y.T.to_csv()