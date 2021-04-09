import csv
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def write_into_csv(csv_data):

    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="download.csv"'

    return response


def data_preprocessing(X, file_path, wl_corr=None,):

    if wl_corr == None:
        wl_corr = X.columns[-1]

    y = X.copy()
    y -= y.iloc[0, :]
    y.drop(y.index[0], inplace=True)
    y = y.sub(y[wl_corr], axis='index')
    y.T.to_csv(file_path)

    return 


def data_vis(file_path):
    
    X = pd.read_csv(file_path, index_col=0).T
    t = X.index.values.astype('float32')
    wl = X.columns.values.astype('float32')

    f = plt.figure(figsize=(6, 6), dpi=100)
    gs = f.add_gridspec(1, 1)

    with sns.axes_style("whitegrid"):

        ax = f.add_subplot(gs[0, 0])
        for i in range(len(t)):
            ax.plot(wl, X.iloc[i, :], lw=1, label=int(t[i]))
            ax.set_xlim([320, 700])
            ax.set_ylim([0, 0.1])
            ax.set_ylabel('Absorbance')

        ax.legend(loc='upper left',
                bbox_to_anchor=(1.05, 1.05),
                frameon=False
                )
        
        f.savefig(file_path + '/fig.png')
    
    return
