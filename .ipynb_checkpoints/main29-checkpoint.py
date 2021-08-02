import plotly.graph_objects as go

labels = ['台北', '新竹', '台中', '高雄']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()