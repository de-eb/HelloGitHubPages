import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 25, 60]),
)
fig.show()

fig.write_html("test.html") # test.htmlとして保存