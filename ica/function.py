import csv
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import pyper
import os
import io
import matplotlib
matplotlib.use("Agg")
import base64


def get_image():
 buffer = io.BytesIO()
 plt.savefig(buffer, format='png')
 image_png = buffer.getvalue()
 graph = base64.b64encode(image_png)
 graph = graph.decode('utf-8')
 buffer.close()
 return graph



def data_vis(file_path):
    
    X = pd.read_csv(file_path, index_col=0).T
    t = X.index.values.astype('float32')
    wl = X.columns.values.astype('float32')

    f = plt.figure(figsize=(6, 3), dpi=100)
    gs = f.add_gridspec(1, 1)

    with sns.axes_style("whitegrid"):

        ax = f.add_subplot(gs[0, 0])
        for i in range(len(t)):
            ax.plot(wl, X.iloc[i, :], lw=1, label=int(t[i]), color=cm.gray(i/len(t)))
            ax.set_xlim([320, 700])
            ax.set_xlabel('Wavelength / nm')
            ax.set_ylabel('Signal intensity')
        plt.tight_layout()
        


def icar(file_path, algo, n_components):
    data = pd.read_csv(file_path)

    # Rのインスタンスを作る
    r = pyper.R(use_pandas='True')

    # PythonのオブジェクトをRに渡す
    r.assign('data', data)
    r.assign('n_components', n_components)

    # Rのコードを実行する
    r("library(ica)")
    r("wl <- data[c(136:511),1]")
    r("X  <- data[c(136:511),-1]")

    if algo == 'FastICA':
        r("a <- icafast(X, n_components)")
    elif algo == 'InfoMax':
        r("a <- icaimax(X, n_components)")
    else:
        r("a <- icajade(X, n_components)")

    r("ics <- cbind(wl, a$S)")

    # Pythonでrのオブジェクトを読む
    ics = r.get("ics")
    ics_df = pd.DataFrame(ics)

    return ics_df



