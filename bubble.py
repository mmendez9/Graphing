import plotly as py
from plotly.graph_objs import *

fistLine = Scatter (
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],

    marker = dict(
        color = ['red', 'blue', 'yellow', 'green'],
        size = [30, 80, 40, 234]),
    mode = 'markers'
)

data = Data([fistLine])

graphLayout = Layout(
    title = 'Bubble Graph',
    xaxis = dict(title = 'Number of people'),
    yaxis = dict(title = 'Number of hours worked')
)

fig = Figure(data = data, layout = graphLayout)

py.offline.plot(fig, filename='bubble.html')
