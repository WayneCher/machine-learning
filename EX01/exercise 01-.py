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

# Scatter plot the data

row_num = df.Area.size
x1 = df['Area'].values
x2 = df['Bedroom'].values
y = df['Price'].values
scatter_plot(x1,y, size = 20, marker = 'x')
scatter_plot(x2,y, size = 20, marker = 'x')

# iteration
def iter_fun(alpha = 0.01, count = 0, ):
    df_theta = np.zeros(df.shape[1])
    #initialize J function
    func(df_theta, 


