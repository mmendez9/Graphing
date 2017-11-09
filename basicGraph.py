import plotly as py
from plotly.graph_objs import *

firstLine = Scatter(
    x=[1, 2, 3],
    y=[10, 15, 20]
)

data = Data([firstLine])

py.offline.plot(data, filename = 'firstGraph.html')

