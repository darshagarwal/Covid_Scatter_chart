import pandas as pd
import plotly.express as px

df= pd.read_csv("/Users/neha/Downloads/PythonWorkspaceDarsh/pro 103/Copy+of+data+-+data.csv")
fig= px.scatter(df,x="date",y="cases",size="cases",color="country",size_max=20)
fig.show()