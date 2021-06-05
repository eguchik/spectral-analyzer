import pandas as pd
import pyper
import matplotlib


def icar(file_path, algo, n_components, wl_range_start, wl_range_end):
    data = pd.read_csv(file_path, index_col=0).T
    data = data.loc[: ,wl_range_start : wl_range_end].T
    wl = data.index.values.astype('float32')

    # Rのインスタンスを作る
    r = pyper.R(use_pandas='True')

    # PythonのオブジェクトをRに渡す
    r.assign('data', data)
    r.assign('wl', wl)
    r.assign('n_components', n_components)

    # Rのコードを実行する
    r("library(ica)")
    r("X  <- data")

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



