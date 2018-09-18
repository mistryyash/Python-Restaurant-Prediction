# coding: utf-8

import matplotlib.pyplot as py
import seaborn as sb
import pandas as pd
import numpy as np

df=pd.read_csv('Restaurant.csv')

def plot1():
    sb.countplot(x='day',hue='time' ,data=df)
def plot2():
    sb.swarmplot(x="day", y="total_bill", hue="sex", data=df);
def plot3():
    sb.swarmplot(x="day", y="total_bill", hue="sex", data=df, dodge=True);
def plot4():
    sb.swarmplot(x="day", y="total_bill", data=df)
def plot5():
    sb.swarmplot(x="total_bill", y="day", data=df)
def plot6():
    sb.swarmplot(x="time", y="tip", data=df, order=["Dinner", "Lunch"])
def plot7():
    sb.factorplot(x="time", y="total_bill", hue="smoker",col="day", data=df, kind="swarm", size=10, aspect=0.7);
def plot8():
    sb.factorplot(x="sex", y="total_bill", hue="smoker", kind="swarm", col="time", data=df);
    
# Initialize dataframe
df2 = df.loc[df['time'] == 'Dinner'];

# Saving Image
py.savefig("bill_smoker.png")

# Method Call
plot1()