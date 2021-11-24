# Real condition with non-zero of theta0 and theta1

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
from mpl_toolkits import mplot3d
import os 

# Read the data from file

dir = os.path.join(os.getcwd(),'ex1data1.txt')

# Use Pandas package
df = pd.read_csv(dir, sep = ',', names = ['Profit','Popu'] )

# Scatter plot function
def scatter_plot(x,y,size = 10, marker = '*', color = 'red'):
    plt.scatter(x,y,s = size, marker = marker, c = color)
    plt.xlabel('Population in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.plot(x, 3.5 + 0.7 * x)
    plt.show()
    
row_num = df.Profit.size
# Plot the data
x = df['Popu'].values
y = df['Profit'].values
scatter_plot(x,y, size = 20, marker = 'x')

# Equations
def deriva_0(theta0,theta1,x,y):
    sum = 0
    for i in range(row_num):
        sum = sum + (theta0 + theta1 * x[i] - y[i])
    return sum / row_num

def deriva_1(theta0,theta1,x,y):
    sum = 0
    for i in range(row_num):
        sum = sum + (theta0 + theta1 * x[i] - y[i]) * x[i]
    return sum / row_num

# J(theta) definition
def J(theta0,theta1,x,y):
    sum = 0
    for i in range(row_num):
        sum = sum + np.power((theta0 + theta1 * x[i] - y[i]),2)
    return sum / (2 * row_num)

# plot function
def plot(x,y):
    plt.plot(x,y)
    plt.xlabel('theta')
    plt.ylabel('J(theta)')
    plt.show()

# iteration = 30000
alpha = 0.0001
df_theta = pd.DataFrame(columns = ['theta0','theta1'])
J1 = []
theta0 = 0
theta1 = 0
for i in range(1500):
    new = pd.Series({'theta0':theta0,'theta1':theta1})
    df_theta = df_theta.append(new,ignore_index = True)
    J1.append(J(theta0,theta1,x,y))
    temp1 = theta0 - deriva_0(theta0,theta1,x,y) * alpha
    temp2 = theta1 - deriva_1(theta0,theta1,x,y) * alpha
    theta0 = temp1
    theta1 = temp2

plot(df_theta['theta0'].values,J1)
the0 = df_theta['theta0'].values
the1 = df_theta['theta1'].values
print(the0[-1],the1[-1],len(the0),len(the1))

# plot 3d
fig = plt.figure()
#ax = Axes3D(fig,auto_add_to_figure=False)
#fig.add_axes(ax)
ax = plt.axes(projection= '3d')
X = np.array(the0)
Y = np.array(the1)
X,Y = np.meshgrid(X,Y)
ax.contour3D(X,Y,J(X,Y,x,y),50,cmap='binary')
plt.show()

