import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot


def plot_data(path, method):

    fig = go.Figure()
    
    if method == 0:
        data = pd.read_csv(path, index_col=0)
        for i in data.columns:
            fig.add_trace(go.Scatter(x=data.index.astype('float'), y=data[i], mode='lines', name=i))
    else:
        data = pd.read_csv(path, index_col=0).T
        for i in data.columns:
            fig.add_trace(go.Scatter(x=data.index.astype('float'), y=data[i], mode='markers+lines', name=i, visible='legendonly'))

    fig.update_layout(template='simple_white')
    fig.layout.xaxis.update({'title': 'Wavelength (nm)'})
    fig.layout.yaxis.update({'title': 'Absorbance'})
    fig.update_xaxes(title_font_family="Arial")
    fig.update_yaxes(title_font_family="Arial")
    plot_fig = plot(fig, output_type='div', include_plotlyjs=False)

    return plot_fig
