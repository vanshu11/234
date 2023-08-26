import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
dataset=pd.read_csv('projectC234_EPL.csv')
gc=dataset['Goals']
a=gc.groupby(dataset['Club'])
b=a.sum()
c=b.sort_value(ascending=False)
print("primier league goal of each club:",c)
d=dataset.sort_values(by=['Goals'],ascending=False)[:10]
print("top goal scorer in primier league:",d)
fig=px.bar(d,x='Name',y='Goals',color='Goals',hover_data=['Club','Age'],text='Goals')
fig.show()
