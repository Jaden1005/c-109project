import random
import statistics
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as fx
import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
stdev=statistics.stdev(data)
print("Mean is:",mean)
print("Median is:",median)
print("Mode is:",mode)
print("Standard Deviation is:",stdev)
first_stdev_start,first_stdev_end=mean-stdev,mean+stdev
second_stdev_start,second_stdev_end=mean-(2*stdev),mean+(2*stdev)
third_stdev_start,third_stdev_end=mean-(3*stdev),mean+(3*stdev)
fig=fx.create_distplot([data],["result"])
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="first_stdev_start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="first_stdev_end"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="second_stdev_start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="second_stdev_end"))
fig.add_trace(go.Scatter(x=[third_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="third_stdev_start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="third_stdev_end"))
fig.show()
list_data_1_stdev=[result for result in data if result>first_stdev_start and result<first_stdev_end]
list_data_2_stdev=[result for result in data if result>second_stdev_start and result<second_stdev_end]
list_data_3_stdev=[result for result in data if result>third_stdev_start and result<third_stdev_end]
print("{}% of data lies within one standard deviation".format(len(list_data_1_stdev)*100/len(data)))
print("{}% of data lies within second standard deviation".format(len(list_data_2_stdev)*100/len(data)))
print("{}% of data lies within third standard deviation".format(len(list_data_3_stdev)*100/len(data)))