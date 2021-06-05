import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.io as pio


#layout
pio.templates.default = "simple_white"


def plot_data(path):
    data = pd.read_csv(path, index_col=0)

    fig = go.Figure()
    for i in data.columns:
        fig.add_trace(go.Scatter(x=data.index, y=data[i], mode='lines', name=i))
    fig.layout.xaxis.update({'title': 'Wavelength (nm)'})
    fig.layout.yaxis.update({'title': 'Sinal intensity'})
    plot_fig = plot(fig, output_type='div', include_plotlyjs=False)

    return plot_fig
