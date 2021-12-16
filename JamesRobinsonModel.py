# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:05:32 2021

@author: Ben Lanoue
This program will use linear regression to calculate
James Robinson's rushing yards.
This will be a single attribute supervised model
consisting of rush attempts as the input and the
rushing yards as the output. 
This program will utilize Andrew Ng's lecture model
and theory. The model will make it so for a given
amount of rush attempts, there is a calculated amount
of rushing yards. Univariate linear regression
This program will also use panda's dataframe 
to read the data as a csv file
"""
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# amount of elements in the data
m = 0
#theta0 is b and theta1 is m in y=mx+b
theta0 = 0
theta1 = 1
#alpha, the learning rate
a = 0.002
jrpd = pd.read_csv("JamesRobinson.csv",index_col=0)
xaxis = []
yaxis = []

costValues = []
xCostValues = []

for index, row in jrpd.iterrows():
    xaxis.append(int(row[0]))
    yaxis.append(int(row[1]))
    m += 1
#plt.plot(xaxis,yaxis,"bo")

def cost(n,t0,t1):
    temp = 0
    for num in range(n):
        temp = temp + ((hypothesis(xaxis[num], t0, t1) - yaxis[num])*(hypothesis(xaxis[num], t0, t1) - yaxis[num])/(2*n))
    
    return temp

#this will take an input of x values and output
#a predicted y output
def hypothesis(x,t0,t1):
    return x*t1+t0
    

def minimize(t0,t1,T,alpha):
    for i in range(T):
        temp0 = 0
        temp1 = 0
        
        for n in range(m):
            temp0 = temp0 + (hypothesis(xaxis[n],t0,t1) - yaxis[n])/m
            temp1 = temp1 + ((hypothesis(xaxis[n], t0,t1)-yaxis[n])* xaxis[n])/m

        t0 = t0 - (temp0*alpha)
        t1 = t1 - (temp1*alpha)
        
        costValues.append(cost(m,t0,t1))
        xCostValues.append(i)
    print(t0,t1)
    return


def main():
    minimize(theta0,theta1,40000,a)
    #plt.plot(xCostValues,costValues)
    #plt.title("Cost value through Iterations")
    #plt.xlabel("Iterations")
    #plt.ylabel("Cost Value")
    plt.plot(xaxis,yaxis,"bo")
    x = np.linspace(0,25)
    y = 6.2568*x + -16.289
    plt.plot(x,y,"-r")
    


main()
