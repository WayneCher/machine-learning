# Some functions used in homework

from matplotlib import pyplot as plt
import numpy as np

# Scatter plot to validate the correction 
# size is the plot size of dots, marker is the shape of dots 
def scatter_plot(x, y, size = 10, marker = '*', color = 'red', x_label = ' ', y_label = ' ',function = ' '):
    plt.scatter(x,y,s = size, marker = marker, c = color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if function != ' ':
        plt.plot(function)
    plt.show()

# linear plot
def plot(x, y, x_label, y_label):
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# Derivative function
class func(object):

    def __init__(self, theta, var, row_num = 0):
        theta = np.array(self.theta)
        var = np.array(self.var.loc[0])
        for i in var.loc[1:]:
            var = np.row_stack((var,i))
        var = np.insert(var, 0, values = np.ones((1,row_num)), axis = 1)
        self.theta = theta
        self.var = var
        
    def sum_part(self,theta_flag = 0):
        sum = 0
        for i in range(row_num):
            sum = sum + (self.var * self.theta.T - self.var[i][-1]) * self.var[i][theta_flag]
        return sum / row_num

    def J(self):
        sum = 0
        for i in range(row_num):
            sum = sum + np.power((self.var * self.theta.T - self.var[i][-1]),2)
        return sum / (2 * row_num)



        
    
    

    
