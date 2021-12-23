from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
from mpl_toolkits import mplot3d
import os
from functions import *

# Read the data from file

dir = os.path.join(os.getcwd(),'ex1data2.txt')

# Use pandas package

df = pd.read_csv(dir, sep = ',', names = ['Area','Bedroom','Price'])
df['Area'] = df['Area'] / 1000
df['Price'] = df['Price'] / 1000

# Scatter plot the data

row_num = df.Area.size
x1 = df['Area'].values
x2 = df['Bedroom'].values
y = df['Price'].values

# iteration
def iter_fun(alpha = 0.01, count = 0):
    df_theta = np.zeros(df.shape[1])
    theta_val = np.zeros(df.shape[1])
    j_val = []
    #initialize J function

    f = func(df_theta, df, row_num)
    for i in range(count):   
        j_val.append(f.j())
        for i in range(len(df_theta)):
            df_theta[i] = df_theta[i] - alpha * f.sum_part(i)
        theta_val = np.row_stack((theta_val, df_theta))
        f.set_theta(df_theta)
    return j_val, theta_val

#main function
if __name__ == '__main__':
    val = iter_fun(count = 20000)
    counts = np.arange(1,20001,1)
    print(val[1][-1])
    plot(counts, val[0], 'counts', 'J Value')
    scatter_plot(x1, x2, y, size = 20, marker = 'x', theta = [89.59, 139.21, -8.74])
    print(vali(df))
    
    


