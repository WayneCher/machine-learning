#exercise 01

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

# 2.1 Before task, To better understand the data
# Visualizing the data with a scatter plot

# Read the data from file

dir = 'D:/Wayne/Miscellaneous/新建文件夹/machine-learning/EX01/ex1data1.txt' # replace with your path

''' Traditional method
data_list = []
with open(dir) as f:
    for eachLine in f:
        eachLine = eachLine.strip('\n')
        data = eachLine.split(',')
        data_list.append(data)
df = pd.DataFrame(data_list, columns = ['Profit','Population']) '''

# Use Pandas package
df = pd.read_csv(dir, sep = ',', names = ['Profit','Popu'] )
#print(df)

# Scatter plot function
def scatter_plot(x,y,size = 10, marker = '*', color = 'red'):
    plt.scatter(x,y,s = size, marker = marker, c = color)
    plt.xlabel('Population in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.plot(x, 1.0184 * x)
    plt.show()

# Plot the data
x = df['Popu'].values
y = df['Profit'].values
scatter_plot(x,y, size = 20, marker = 'x')


# 2.2 Linera regression with one variable
# Equation with simplified theta0 = 0 

row_num = df.Profit.size
# derivative part of theta1
def deriva(theta1,x,y):
    sum = 0
    for i in range(row_num):
        sum = sum + (theta1 * x[i] - y[i]) * x[i]
    return sum / row_num

# J(theta) definition
def J(theta1,x,y):
    sum = 0
    for i in range(row_num):
        sum = sum + math.pow((theta1 * x[i] - y[i]),2)
    return sum / (2 * row_num)
    
#theta1 = theta1 - alpha * deriva(theta1,x,y)

# plot function
def plot(x,y):
    plt.plot(x,y)
    plt.xlabel('theta')
    plt.ylabel('J(theta)')
    plt.show()

''' test the function 
alpha = 0.01
theta1 = 0
print(J(theta1,x,y)) '''

# iteration = 1500
alpha = 0.0001
theta = []
J1 = []
theta1 = 0
for i in range(1500):
    theta.append(theta1)
    J1.append(J(theta1,x,y))
    temp = theta1 - alpha * deriva(theta1,x,y)
    theta1 = temp
plot(theta,J1)
print(theta[-1])

# Real condition with non-zero of theta0 and theta1 shows in EXERCISE 01-2





