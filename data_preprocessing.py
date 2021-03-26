import numpy as np
import pandas as pd


def preprocessing(X, wl_corr=None):
    if wl_corr == None:
        wl_corr = X.columns[-1]

    y = X.copy()
    y -= y.iloc[0, :]
    y.drop(y.index[0], inplace=True)
    y = y.sub(y[wl_corr], axis='index')

    return y
