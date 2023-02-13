import pandas as pd
import plotly.express as px
df = pd.read_csv('sample_sort.csv')

fig = px.bar(df, x="v1", y="v1", animation_frame="step", range_y=[0,10])
fig.show()