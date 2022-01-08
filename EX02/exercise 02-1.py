from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
from mpl_toolkits import mplot3d
import os
from functions import *

# Read the data from file

dir = os.path.join(os.getcwd(),'ex2data1.txt')

# Use pandas package

df = pd.read_csv(dir, sep = ',', names = ['Test1','Test2','Admin'])

# Scatter plot the data

row_num = df.Test1.size
x = df['Test1'].values
x = np.column_stack((x, df['Test2'].values))
x = x / 10
y = df['Admin'].values
y = y.reshape(len(y),1)
row_num = y.shape[0]

# iteration
def iter_fun(alpha = 0.1, count = 0):
    df_theta = np.zeros((df.shape[1], 1))
    theta_val = np.zeros(df.shape[1])
    j_val = []
    #initialize J function
    f = func(df_theta, x, y, row_num = row_num, alpha = alpha)
    for i in range(count):
        val = f.com_theta()
        theta_val = np.row_stack((theta_val, val[0].T))
        j_val.append(val[1])
        f.set_theta(val[0])     
    return j_val, theta_val

#main function
if __name__ == '__main__':
    plt.ylim(30,100)
    plt.scatter(df['Test1'].values, df['Test2'].values, c = df['Admin'].values)
    x1 = np.arange(30, 101, 1)
    plt.plot(x1, (210 - 1.73 * x1) / 1.68)
    plt.show()
    ''''val = iter_fun(count = 30000)
    counts = np.arange(1,30001,1)
    print('val',val[1][-1])
    print('cost',val[0][-1])
    plot(counts, val[0], 'counts', 'J Value')
    #scatter_plot(x1, x2, y, size = 20, marker = 'x', theta = [22.1,72.4,54.6])
'''
    
    


