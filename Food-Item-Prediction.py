# coding: utf-8

import seaborn as sb
import pandas as pd
import numpy as np
import math 

df=pd.read_csv('Restaurant.csv')

df.replace({ 'sex': {'Male':0 , 'Female':1} ,
            'smoker' : {'No': 0 , 'Yes': 1},
            'time' : {'Lunch': 0 , 'Dinner': 1},
            'day': {'Sun':7 , 'Sat':6, 'Fri':5, 'Thur':4},
            'food': {'poutine':1 , 'pizza':2, 'burger':3, 'shawarma':4,'bagel':5 , 'tacos':6, 'nachos':7, 'butter tarts':8,
                     'burritos':9 }
            } ,inplace=True)

def food(p):
    if p==1:
        print("Predicted food : Poutine")
    elif p==2:
        print("Predicted food : Pizza")
    elif p==3:
        print("Predicted food : Burger")
    elif p==4:
        print("Predicted food : Shwarma")
    elif p==5:
        print("Predicted food : Bagel")
    elif p==6:
        print("Predicted food : Tacos")
    elif p==7:
        print("Predicted food : Nachos")
    elif p==8:
        print("Predicted food : Butter-Tarts")
    else:
        print("Predicted food : Burrito")
        
X = df[['size','day','time']]
Y = df[['food']]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test , y_train , y_test = train_test_split(X,Y,test_size=0.25,random_state=26)

model = LinearRegression()
model.fit(X_train, y_train)

predictions=model.predict(X_test)

# Customer Table Size = 3, Day = Saturday, Time = Dinner
myvals = np.array([3,6,1]).reshape(1,-1)
p=model.predict(myvals)
food(int(p))