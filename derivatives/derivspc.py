import numpy as np
import pandas as pd
from scipy import signal


class DerivSpc:
    def __init__(self, n_differential, polyorder, window_length, n_smooth):
        self.n_differntial = n_differential
        self.polyorder = polyorder
        self.window_length = window_length
        self.n_smooth = n_smooth


    def fit(self, X):
        y = X.copy().values
        n_samples = y.shape[1]

        for i in range(n_samples):
            for j in range(self.n_differntial):
                y[:, i] = np.gradient(y[:, i])
            for k in range(self.n_smooth):
                y[:, i] = signal.savgol_filter(y[:, i], self.window_length, self.polyorder)
        
        return pd.DataFrame(y, index=X.index, columns=X.columns)

