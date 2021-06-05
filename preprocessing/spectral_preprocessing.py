import pandas as pd

def preprocessing(file_path):
    data = pd.read_csv(file_path, index_col=0)
    data = data.sub(data.iloc[:, 0], axis='index')
    data = data.sub(data.loc[700, :], axis="columns")
    data.drop(columns=data.columns[0], inplace=True)

    return data