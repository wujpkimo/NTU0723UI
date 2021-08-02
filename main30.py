import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.DataFrame({
    "Station": ['南港', '台北', '板橋', '南港', '台北', '板橋'],
    "Provider": ['Uber', 'Uber', 'Uber', 'Line', 'Line', 'Line'],
    "Passenger": [2, 7, 3, 8, 2, 4]
})

fig = px.bar(df, x='Station', y="Provider", color="Passenger", barmode="group")
fig = go.Figure()
description = "Provider=%s<br>Station=%%{x}<br>Passenger=%%{y}"
for provider, group in df.groupby("Provider"):
    fig.add_trace(go.Bar(x=group["Station"], y=group["Passenger"], name=provider,
                         hovertemplate=description % provider))

fig.update_layout(legend_title_text="Provider")
fig.update_xaxes(title_text="Station")
fig.update_yaxes(title_text="Passenger k/times")
fig.show()
