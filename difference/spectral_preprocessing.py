import pandas as pd

def preprocessing(data, wl_corr):
    data = data.sub(data.iloc[:, 0], axis='index')
    data = data.sub(data.loc[wl_corr, :], axis="columns")
    data.drop(columns=data.columns[0], inplace=True)

    return data